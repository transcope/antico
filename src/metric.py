""" Metrics to detect suspiciousness of cards. Multiple choices are available. """

import numpy as np


__all__ = ['cal_metrics']


def cal_metrics (exps, n_days, quant, choice=None):
    """ Calculate suspiciousness metrics aimed at specified credit card
    Args:
       exps: transaction data with timestamps, defined as: [(1000, '2021-01-01'), (10.5, '2021-01-02')]
       n_days: specific time span (unit: day)
       quant: credit limit
       choice: optional, metric choice. If None, using default metric in config. 
    Returns:
       creditcard suspiciousness score 
    """
    import pandas as pd
    #
    from ..config import metric
    from ..config import date_format as fmt
    #
    f = lambda a,b: a * b
    # temperal aggregation metric
    m_key = (choice if choice else metric)
    cal_metric = (metric_dict[m_key] if m_key in metric_dict else None)
    #
    df = pd.DataFrame(exps, columns=["transaction", "timestamp"])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format = fmt)
    # cluster transactions by day
    df_group = df.groupby([df['timestamp'].dt.date])['transaction'].agg(['sum','count'])
    #
    sums = np.zeros(n_days)
    for (ts, row) in df_group.iterrows():
        # Warning: the coding is based on the assumption that time start from
        #          the beginning of month and only suit for one month.
        idx = ts.day - 1
        sums[idx] = row['sum']
    # intensiveness
    t_agg_m = cal_metric(sums)
    # majority
    c_opy_m = sum(sums) / float(quant)
    return (t_agg_m, c_opy_m)


def cal_vc(data):
    """ Calculate variation coefficient 
    Args:
       data: dataset
    Returns:
       variation coefficient score 
    """
    from scipy import stats
    #
    mats = np.zeros((1,len(data)))
    mats[0,1] = sum(data)
    max_v = stats.variation(mats.ravel())
    min_v = 0
    rst =  (stats.variation(data) - min_v) / (max_v - min_v)
    return rst 


def cal_kurtosis(data):
    """ Calculate kurtosis
    Args:
       data: dataset 
    Returns: 
       kurtosis score 
    """
    from scipy import stats
    #
    mats = np.zeros((1,len(data)))
    mats[0,1] = sum(data) 
    max_v = stats.kurtosis(mats.ravel(), fisher=False)
    min_v = 0
    rst = (stats.kurtosis(data) - min_v) / (max_v - min_v)
    return rst


def cal_gini_integral(data):
    """ Calculate gini index by integrals.
    Args:
       data: dataset
    Returns: 
       gini score 
    """
    #
    func_name = cal_gini_integral.__name__
    try: 
        cum_vals = np.cumsum(sorted(np.append(data, 0)))
        sum_vals = cum_vals[-1]
        xarray = np.array(range(0, len(cum_vals))) / np.float(len(cum_vals)-1)
        yarray = cum_vals / sum_vals
        B = np.trapz(yarray, x=xarray)
        A = 0.5 - B
        rst = A / (A+B)
    except Exception as e:
        print(e)
        print('[{}] gini: {}'.format(func_name, rst))
    return rst 


def cal_gini_discrete(data):
    """ Calculate gini index in discretized way
    Args:
       data: dataset 
    Returns:
       gini score 
    """
    #
    func_name = cal_gini_discrete.__name__
    try:
        n = len(data)
        # non-decreasing order
        a = sorted(np.append(data, 0))
        rst = 2 * sum(np.array(range(n+1)) * a) / (n * sum(a)) - (n + 1) / n
    except Exception as e:
        print(e)
        print('[{}] gini: {}'.format(func_name, rst))
    return rst


metric_dict = {'vc': cal_vc, 'kurt': cal_kurtosis, 'gini1': cal_gini_integral, 'gini2': cal_gini_discrete}
