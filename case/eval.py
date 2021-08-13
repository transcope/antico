""" evaluate the detection outputs """


def cal_precision_recall_fscore (y_dict, y_pred_dict):
    """ Calculate f-score with precision and recall scores
    Args:
       y_dict: credit cards with ground truth (correct) values, format:
               - key = creditcard id, value = label (1 means fraud, 0 means non-fraud)
       y_pred_dict: credit cards with estimated values by model, format:
               - key = creditcard id, value = estimated value  
    Returns:
       evaluation scores (precision score, recall score, f-score)
    """
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import f1_score
    #
    y_true, y_pred = process(y_dict, y_pred_dict)
    #
    precision = precision_score(y_true, y_pred)
    recall    = recall_score(y_true, y_pred)
    f1_score  = f1_score(y_true, y_pred)
    ret = (precision, recall, f1_score)
    return ret


def process (y, y_pred):
    """ Check and then transform data from dictionary to list.
    Arys:
       y: credit cards with ground truth (correct) values, format: 
          - key = creditcard id, value = ground truth
       y_pred: credit cards with estimated values by model, format:
          - key = creditcard id, value = predicted value
    Return:
       - list of ground truth values
       - list of predicted values 
    """
    func_name = process.__name__
    #
    y_vals = []
    y_pred_vals = []
    for k, v in y_pred.items():
        if k in y:
            y_vals.append(y[k])
            y_pred_vals.append(v)
        else:
            print('[{}] {} is not found '.format(func_name, k))
    return y_vals, y_pred_vals


if __name__ == '__main__':

    import json
    from aco.config import data_path
    from aco.src.util.find import find_data 
    #
    from read import read_card_data
    # load y
    files = ['{}/cards.gz'.format(data_path)]
    cards = read_card_data(files)
    y = {c[0]:c[-1] for c in cards}

    # load y_pred
    res = []
    res_file = 'blocks.json' 
    with open(res_file, 'rb') as f:
        node_set = []
        blocks = json.load(f)
        for blk in blocks:
            vals = find_data(blk, ['Nodes','CreditCard'])
            nodes = []
            for nod in vals:
                if isinstance(nod, list):
                    nodes.append(nod[0])
                if isinstance(nod, str):
                    nodes.append(nod)
            node_set.append(nodes)
        #
        hit_cids = [list(node_set[0])]
        for i in range(1, len(node_set)):
            hit_cids.append(list(set(hit_cids[-1] + node_set[i])))
        for (i, hc) in enumerate(hit_cids):
            y_pred = {cid: 0 for cid in y}
            for cid in hc:
                y_pred[cid] = 1
            score = cal_precision_recall_fscore(y, y_pred)
            res.append(score)
    print('Score (precision, recall, f1 measure): ', res[-1])
