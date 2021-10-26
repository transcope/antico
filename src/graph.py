""" Generate a credit-side bigraph. """


def create_bigraph (exps_data, cards, merchants, args):
    """ Given creditcard transactions, return c2m (creditcard-merchant) bigraph
    Args:
       exps_data: creditcard transactions
       cards:     creditcard infomation, including creditcard id and credit limit 
       merchants: merchant information, including merchant id and prior
       args: runtime parameters including 
             key: Start,    value: specific beginning date 
             key: TimeSpan, value: the set of specific time spans (unit: day)
                  For example, [Jen. Feb. Mar.] is [31, 28, 31]
    Returns:
       c_exps: creditcard-merchant-weight, format: 
               key: creditcard id, value: tuple(merchant id, weight)
       m_exps: merchant-creditcard-weight, 
               key: merchant id,   value: tuple(creditcard id, weight)
    """
    from .util.find import load_param
    from ..config import fusion as default_fusion_key
    #
    func_name = create_bigraph.__name__
    # load and check arguments
    start_t = load_param(args, 'Start')
    spans   = load_param(args, 'TimeSpan')
    if start_t is None or spans is None:
        return None, None
    # adding fusion config
    f_key   = load_param(args, 'Fusion', default_fusion_key)
    # print('[{}] f_key:  {}'.format(func_name, f_key))
    # 
    c_dict = {c[0]: {'Transactions': [], 'Quant': c[1]} for c in cards}
    m_dict = {m[0]: m[-1] for m in merchants}
    m_set = set()
    for val in exps_data:
        cid = val[0]
        mid = val[1]
        exp = val[2]
        ts  = val[3]
        m_set.add(mid)
        c_dict[cid]['Transactions'].append((mid, exp, ts))
    #
    c_exps = {cid:[] for cid in c_dict}
    m_exps = {mid:[] for mid in m_set}
    for cid in c_dict:
        vals = cal_edge_weight(c_dict[cid]['Transactions'], c_dict[cid]['Quant'], start_t, spans, f_key)
        for mid in vals:
            wgt = vals[mid] * m_dict[mid]
            c_exps[cid].append((mid, wgt))
            m_exps[mid].append((cid, wgt))
    return c_exps, m_exps


def cal_edge_weight (exps_data, quant, start_t, spans, f_key):
    """ Given transactions of one creditcard, return creditcard-weight-merchant
    Args:
       exps_data: transactions made by one creditcard, each of which involves 
                  merchant id, transaction, timestamp
       quant: credit limit
       start_t: specific beginning date
       spans: the set of specific time spans (unit: day)
       f_key: fusion option {mul, exp, sig}
    Returns:
       m_dict: merchant-weight, format: 
               key: merchant id, value: weight
    Remark: 
       1. Calculate total suspiciousness 
       2. Distribute the sum into days 
       3. Set transaction suspiciousness 
       4. group and calculate edge weights 
    """
    import numpy as np
    import pandas as pd
    import datetime as dt
    from .metric import cal_metrics
    from .fusion import fusion_dict as f_dict
    #from ..config import fusion as f_key
    #
    from .util.date import cal_interval_days
    from ..config import date_format as fmt1
    from ..config import datetime_format as fmt2
    #
    func_name = cal_edge_weight.__name__
    #
    fusion = (f_dict[f_key] if f_key in f_dict else None)
    #
    start_d = dt.datetime.strptime(start_t, fmt1).date()
    n_days = sum(spans)
    #
    mids = set()
    exps_per_day = [[] for i in range(n_days)]
    for val in exps_data:
        mid = val[0]
        exp = val[1]
        day = dt.datetime.strptime(val[-1], fmt2).date()
        idx = cal_interval_days(day, start_d)
        exps_per_day[idx].append((mid, exp))
        mids.add(mid)
    # Step 1: calculate node suspiciousness
    offsets = [int(i) for i in np.cumsum([0] + spans)]
    m_list = []
    for (i,(a,b)) in enumerate(zip(offsets[:-1], offsets[1:])):
        exps = []
        for (j, vals) in enumerate(exps_per_day[a:b]):
            ts = dt.datetime.strftime(start_d + dt.timedelta(days=a+j), fmt1)
            exps += [(v[-1], ts) for v in vals]
        m_list.append(cal_metrics(exps, spans[i], quant))
    score = fusion(np.array(m_list).T)
    #
    # node suspiciousness to edge suspiciousness
    #
    # Step 2: allocate total suspiciousness to days  
    sum_per_day = []
    for vals in exps_per_day:
        sum_per_day.append(sum([v[-1] for v in vals]))
    sum_per_day = np.array(sum_per_day)
    wgts_per_day = sum_per_day * (score / sum_per_day.sum())
    # Step 3: calculate transaction suspiciousness 
    # rule: each transaction has the same suspiciousness each day 
    m_dict = {mid: [] for mid in mids}
    for (vals, wgt) in zip(exps_per_day, wgts_per_day):
        for v in vals:
            m_dict[v[0]].append(wgt)
    # Step 4: transform transaction suspiciousness into edge suspisiousness
    for mid in m_dict:
        m_dict[mid] = sum(m_dict[mid]) / len(m_dict[mid])
    return m_dict
