# coding=utf-8

""" Evaluate dense subgraph based anti-cashout detection (creditcard-side) """


def run_aco(graph, n_blocks=3, scoring=False):
    """ anti-cashout detection case
    Args:
       graph: graph data
       n_blocks: number of dense subgraph blocks
       scoring: whether output node with scores
    Returns:
       dense blocks 
    """
    from aco.src.detect import detect_multiple 
    from aco.src.detect import detect_multiple_scoring 
    from aco.src.util.mat import transform 
    from aco.src.greedy import fast_greedy_decreasing as eval_func 
    #
    func_name = run_aco.__name__
    #
    detect_blocks = (detect_multiple_scoring if scoring else detect_multiple)
    # transform to dsad graph 
    smat, (cid2idx, idx2cid, mid2idx, idx2mid) = transform(graph)
    # detect blocks
    res = detect_blocks(smat, eval_func, n_blocks)
    # map to node id and output 
    data = []
    for (i,r) in enumerate(res):
        block = r[0]
        score = r[-1]
        if scoring:
            c_set = [(idx2cid[obj[0]], round(obj[1], 4)) for obj in block[0]] 
            m_set = [(idx2mid[obj[0]], round(obj[1], 4)) for obj in block[1]]
        else:
            c_set = [idx2cid[i] for i in block[0]]
            m_set = [idx2mid[i] for i in block[1]]
        data.append({'Subgraph': (len(c_set), len(m_set)), 
                     'Score': score,
                     'Nodes': {'CreditCard': c_set, 'Merchant': m_set}})
        print('[{}] top {}  total_cards: {}  total_merchants: {}  score: {}'.format(func_name, i, len(c_set), len(m_set), round(score, 4)))
    return data


if __name__ == '__main__':
    
    from read import read_c2m_data
    from aco.src.graph import create_bigraph
    #
    from aco.config import data_path
    from aco.config import start_date as start_t
    from aco.config import end_date   as end_t
    from aco.config import time_spans as spans

    # load data 
    c_filenames = ['cards.gz']
    m_filenames = ['merchants.gz']
    t_filenames = ['transactions.gz']
    #
    input_params = {}
    input_params['Card']        = ['{}/{}'.format(data_path, fn) for fn in c_filenames]
    input_params['Merchant']    = ['{}/{}'.format(data_path, fn) for fn in m_filenames]
    input_params['Transaction'] = ['{}/{}'.format(data_path, fn) for fn in t_filenames]
    #  
    cards, merchants, transactions = read_c2m_data(input_params)
    #
    # create bigraph
    args = {'Start': start_t, 'TimeSpan': spans}
    c_exps, m_exps = create_bigraph(transactions, cards, merchants, args) 
    graph = [c_exps, m_exps]
    # dense subgraph detection
    top_n = 3 
    res = run_aco(graph, top_n, True)
    # evaluate 

    # output 
    import json
    output_file = './blocks.json'
    with open(output_file, 'w') as f:
        json.dump(res, f)
