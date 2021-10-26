
from antico.src.util.find import load_param
from antico.src.util.load import *


def read_c2m_data(params):
    """ Load creditcard-merchant transaction data module.
    Args:
       params: settings of data files, format: 
               key = objects {Card, Merchant, Transaction}, values = list of files.
    Return:
       data: list of data, including cards, merchants, transactions 
    """
    #
    func_name = read_c2m_data.__name__
    # load card data
    files = load_param(params, 'Card', [])
    cards = read_card_data(files)
    # load merchant data
    files = load_param(params, 'Merchant', [])
    merchants = read_merchant_data(files)
    # load creditcard-merchant transaction data
    files = load_param(params, 'Transaction', [])
    transactions = read_transaction_data(files)
    #
    print('[{}] cards: {} merchants: {} transactions: {}'.format(func_name, len(cards), len(merchants), len(transactions)))
    return cards, merchants, transactions


def read_card_data(files):
    """ Load creditcard data.
    Args:
        files: list of card info files
    Return:
        card data 
    """
    import gzip
    #
    func_name = read_card_data.__name__
    #
    res = []
    try:
        for fname in files:
            with gzip.open(fname, 'rb') as f:
                for line in f.readlines()[1:]:
                    vals = line.decode().strip().split()
                    cid    = str(vals[0])
                    quant  = int(vals[1])
                    b_date = int(vals[2])
                    d_date = int(vals[3])
                    c_sort = int(vals[4])
                    label  = int(vals[5])
                    res.append((cid, quant, label))
    except Exception as e:
        print('[{}] {}'.format(func_name, e))
    return res


if __name__ == '__main__':
    
    from antico.config import data_path

    c_filenames = ['test_cards.gz']
    m_filenames = ['test_merchants.gz']
    t_filenames = ['test_transactions.gz']
    #
    params = {}
    params['Card']        = ['{}/{}'.format(data_path, fn) for fn in c_filenames]
    params['Merchant']    = ['{}/{}'.format(data_path, fn) for fn in m_filenames]
    params['Transaction'] = ['{}/{}'.format(data_path, fn) for fn in t_filenames]
    #
    cards, merchants, transactions = read_c2m_data(params)
    #print(len(cards), len(merchants), len(transactions))
