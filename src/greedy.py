# coding=utf-8

""" Dense Subgraph based anti-cashout detection. """


def fast_greedy_decreasing(smat):
    """ Fase greedy decrease based dense block algorithm. Return densest block.  
    Avgs:
       smat: coo_matrix, bigraph sparse matrix
    Returns:
       - dense block, including scoure nodes and destination nodes
       - suspiciousness score 
    """
    import numpy as np
    from .tree import MinTree
    #
    func_name = fast_greedy_decreasing.__name__
    #
    (m, n) = smat.shape
    smat_dok = smat.todok()
    smat_lil = smat.tolil()
    t_smat_lil = smat.transpose().tolil()
    # 
    row_set = set(range(0,m))
    col_set = set(range(0,n))
    # evaluate the total suspisiousness of graph  
    score = smat[list(row_set), :][:, list(col_set)].sum(axis=None) 
    best_score = score / (len(row_set) + len(col_set)) 
    best_subgraph = (row_set, col_set) 
    # calculate the suspiniouseness of nodes (total edge weights) 
    # source nodes
    row_deltas = np.squeeze(smat.sum(axis=1).A) 
    # destination nodes
    col_deltas = np.squeeze(smat.sum(axis=0).A)
    # transform to minimum priority tree
    row_mtree = MinTree(row_deltas)
    col_mtree = MinTree(col_deltas)
    #print('max_row_deltas {} max_col_deltas {}'.format(row_deltas.max(), col_deltas.max()))
    #print('min_row_deltas {} min_col_deltas {}'.format(row_deltas.min(), col_deltas.min()))
    # 
    del_n = 0
    deleted = [] 
    best_del_n = 0
    cnt = 0
    while row_set and col_set: # terminal condition
        row_idx, row_delt = row_mtree.getMin()
        col_idx, col_delt = col_mtree.getMin()
        #print('iter: {}'.format(cnt))
        #print('row_delt {} col_delt {}'.format(row_delt, col_delt))
        # update priority tree
        if row_delt <= col_delt:
            score -= row_delt
            #print('total rows: {} row_idx: {}'.format(len(smat_lil.rows), row_idx))
            for (i,v) in zip(smat_lil.rows[row_idx], smat_lil.data[row_idx]):
                col_mtree.changeVal(i, -v)
            row_set -= {row_idx}
            row_mtree.changeVal(row_idx, float('inf'))
            deleted.append((0, row_idx))
        else:
            score -= col_delt
            for (i,v) in zip(t_smat_lil.rows[col_idx], t_smat_lil.data[col_idx]):
                row_mtree.changeVal(i, -v)
            col_set -= {col_idx}
            col_mtree.changeVal(col_idx, float('inf'))
            deleted.append((1, col_idx))
        #print('deleted: {} {}'.format(['row','col'][deleted[-1][0]], deleted[-1][-1]))
        # recording  
        del_n += 1
        iter_score = score / (len(row_set) + len(col_set)) 
        if iter_score > best_score:
            best_score = iter_score
            best_del_n = del_n 
        cnt += 1
    #
    # reset the best row and column sets
    best_row_set = set(range(m))
    best_col_set = set(range(n))
    best_sets = [best_row_set, best_col_set]
    for i in range(best_del_n):
        best_sets[deleted[i][0]].remove(deleted[i][1]) 
    #print('[{}] delete nodes: cards {}/{} merchants {}/{} '.format(func_name, len(deleted[0]), m, len(deleted[1]), n))
    return (best_row_set, best_col_set), best_score
