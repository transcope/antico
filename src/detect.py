# coding=utf-8

""" Densed subgraph based anti-cashout detection """


def detect_multiple(smat, eval_func, top_n):
    """ Detect top n dense blocks based on given suspiciousness function.
    Args:
       smat: coo_matrix, creditcard-merchant bigraph based weight (sparse) matrix
       eval_func: func, objective function
       top_n: int, the number of densest blocks 
    Returns:
       blocks: list<(list<source_node>, list<destination_node>), score>, detected blocks with suspiciousness score """
    # mcur = smat.copy().tolil()
    mcur = smat.tolil(copy=True)
    #    
    blocks = []
    for i in range(top_n):
        ((src_nodes, dst_nodes), score) = eval_func(mcur)
        #print (i, score)
        blocks.append(((src_nodes, dst_nodes), score))
        mcur = del_block(mcur, src_nodes, dst_nodes)
    return blocks


def del_block(mcur, row_set, col_set):
    """ Delete subgraph.
    Args:
       mcur: graph data in sparse matrix
       row_set: list of row node index
       col_set: list of column node index 
    Returns:
       the rest graph data, represented by lil_matrix
    """
    (rs, cs) = mcur.nonzero()
    for i in range(len(rs)):
        if rs[i] in row_set and cs[i] in col_set:
            mcur[rs[i], cs[i]] = 0
    return mcur.tolil()


def detect_multiple_scoring(smat, eval_func, top_n):
    """ Detect top n dense blocks based on given suspiciousness function
    Args:
       smat: creditcard-merchant bigraph based weight (sparse) matrix
       eval_func: objective function
       top_n: the number of densest blocks 
    Returns:
       - densent subgraphs, including source nodes and destination nodes
       - suspiciousness score of each subgraph 
    """
    mcur = smat.tolil(copy=True)
    #
    blocks = []
    for i in range(top_n):
        ((row_set, col_set), score) = eval_func(mcur)
        # scoring and then update matrix 
        src_degs = {idx: 0.0 for idx in row_set} 
        dst_degs = {idx: 0.0 for idx in col_set} 
        (rs, cs) = mcur.nonzero()
        for i in range(len(rs)):
            if rs[i] in row_set and cs[i] in col_set:
                val = mcur[rs[i], cs[i]]
                src_degs[rs[i]] += val 
                dst_degs[cs[i]] += val 
                # then delete transaction edge
                mcur[rs[i], cs[i]] = 0
        src_nodes = [(k, src_degs[k]) for k in src_degs]
        dst_nodes = [(k, dst_degs[k]) for k in dst_degs]
        blocks.append(((src_nodes, dst_nodes), score))
    return blocks
