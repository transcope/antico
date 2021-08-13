# coding=utf-8
  

def load_param(data, key, value = None):
    """ Load paramter.
    Args:
       data: paremeter dictionary
       key:  key value
       value: if no key is found in data, then return default value (default: None)
    Returns:
       parameter value
    """
    rst = (data[key] if key in data else value)
    return rst


def find_data(data, keys, value = None):
    """ Find directionary based on the given set of keys in order.
    Args:
       data: nested dictionary
       keys: the chain of keys
       value: if no key is found in data, then return default value (default: None) 
    Returns:
       result value
    """
    vals = data
    for k in keys:
        if k in vals:
            vals = vals[k]
        else:
            return value
    return vals
