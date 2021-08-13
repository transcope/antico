""" Sparse Matrix Utils """

from scipy import sparse

__all__ = ['transform']


def transform(graph):
    """ Transform to data structure for algorithm.
    Args:
       graph: graph data, including  
       - creditcard-merchant-weight, format: 
         key: creditcard id, value: tuple(merchant id, weight)
       - merchant-creditcard-weight, 
         key: merchant id,   value: tuple(creditcard id, weight)
    Returns:
       - creditcard-merchant bigraph based weight (sparse) matrix
       - maps between id and index
    """
    func_name = transform.__name__
    # 
    c_exps = graph[0]
    m_exps = graph[1]
    # unify node id to index
    idx2cid = list(c_exps.keys())
    cid2idx = {cid:idx for (idx,cid) in enumerate(list(c_exps.keys()))}
    idx2mid = list(m_exps.keys())
    mid2idx = {mid:idx for (idx,mid) in enumerate(list(m_exps.keys()))}
    #
    srcs, dsts, wgts = [], [], []
    for cid in c_exps.keys():
        c_idx = cid2idx[cid]
        for (mid, wgt) in c_exps[cid]:
            m_idx = mid2idx[mid]
            srcs.append(c_idx)
            dsts.append(m_idx)
            wgts.append(wgt)
    smat = list_to_sparse_matrix(srcs, dsts, wgts)
    (n,m) = smat.shape
    #print('cards: {}  merchant: {}  transactons: {}'.format(n, m, len(smat.data)))
    return smat, (cid2idx, idx2cid, mid2idx, idx2mid)


def list_to_sparse_matrix(srcs, dsts, wgts, shape=None):
    """ Transform data to sparse matrix
    Args:
       srcs: list of source node id (index) 
       dsts: list of destination node id (index) 
       wgts: list of edge weights
    Returns:
       sparse matrix 
    """
    # node id should be its index    
    if shape is None:
        m = max(srcs) + 1
        n = max(dsts) + 1
    else:
        m = shape[0]
        n = shape[1]
    smat = sparse.coo_matrix((wgts, (srcs, dsts)), shape=(m, n))
    return smat.astype('float')

