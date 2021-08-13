""" load card, merchant, transaction data """

import gzip

def read_card_data(files):
    """ Load creditcard data.
    Args:
       files: list of card info files
    Returns:
       cards: card data 
    """
    func_name = read_card_data.__name__
    #
    cards = []
    try:
        for fname in files:
            with gzip.open(fname, 'rb') as f:
                for line in f.readlines()[1:]:
                    vals = line.decode().strip().split()
                    cid = str(vals[0])
                    quant = float(vals[1])
                    cards.append((cid, quant))
    except Exception as e:
        print('[{}] {}'.format(func_name, e))
        print('[{}] {}'.format(func_name, fname))
    return cards


def read_merchant_data(files):
    """ Load merchant data.
    Args:
       files: list of merchant info files
    Returns:
       merchants: merchant data 
    """
    func_name = read_merchant_data.__name__
    #
    merchants = []
    try:
        for fname in files:
            with gzip.open(fname, 'rb') as f:
                for line in f.readlines()[1:]:
                    vals = line.decode().strip().split()
                    mid = str(vals[0])
                    prior = float(vals[1])
                    merchants.append((mid, prior))
    except Exception as e:
        print('[{}] {}'.format(func_name, e))
        print('[{}] {}'.format(func_name, fname))
    return merchants


def read_transaction_data(files):
    """ Load transaction data.
    Args:
       files: list of transaction data files
    Returns:
       transations: transaction data 
    """
    func_name = read_transaction_data.__name__
    #
    transactions = []
    try:
        for fname in files:
            with gzip.open(fname, 'rb') as f:
                for line in f.readlines()[1:]:
                    vals = line.decode().strip().split()
                    obj_a = str(vals[0])
                    obj_b = str(vals[1])
                    exp = float(vals[2])
                    ts  = str(vals[3])
                    transactions.append((obj_a, obj_b, exp, ts))
    except Exception as e:
        print('[{}] {}'.format(func_name, e))
        print('[{}] {}'.format(func_name, fname))
    return transactions
