""" Rank fusion. Merge multiple metrics to detect suspiciousness. """

from math import e 

__all__ = ['fusion_dict']


def mul_fusion (arr):
    """ Simple fusion by multiple metrics.
    Args:
       arr: metric set 
    Returns:
       fusion score
    """
    # number of metrics 
    n_m = len(arr)
    #
    rst = -1
    if n_m > 0:
        # number of periods 
        n_p = len(arr[0])
        # fusion 
        val = arr[0]
        for i in range(1, n_m):
            val = val * arr[i]
        rst = val.mean()
    return rst


def exp_fusion (arr, b=e):
    """ Metric fusion by exponent function.
    Args:
       arr: metric set
       b: base number (default: e)
    Returns:
       fusion score 
    """
    # number of metrics
    n_m = len(arr)
    #
    rst = -1
    if n_m > 0:
        # number of periods
        n_p = len(arr[0])
        # fusion
        val = arr[0]
        for i in range(1, n_m):
            val = val + arr[i]
        rst = (b**(val - n_p)).mean()
    return rst


def sigmoid_fusion (arr, a=e, b=10, c=20, d=[]):
    """ Metric fusion by sigmoid function, the formula of which is as follows 
             sigmoid = 1 / (1 + a**(b - c * sum(values * weights)))
    Args:
       arr: metric set  
       a: base number (default: e) 
       b: index parameter b
       c: index parameter c
       d: optional, metric weights (default: []) 
    Returns:
       fusion score 
    """
    # number of metrics
    n_m = len(arr)
    #
    rst = -1
    val = []
    if n_m > 0:
        if len(d) == n_m:
            wgts = d 
        else:
            w = 1 / n_m
            wgts = [w for i in range(n_m)]
        # number of periods
        n_p = len(arr[0])
        # fusion
        val = arr[0] * wgts[0]
        for i in range(1, n_m):
            val = val + arr[i] * wgts[i]
        rst = (1 / (1 + a**(b - c*val))).mean()
    return rst


fusion_dict = {'mul': mul_fusion, 'exp': exp_fusion, 'sig': sigmoid_fusion}
