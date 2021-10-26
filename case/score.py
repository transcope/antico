# coding=utf-8


def cal_precision_recall_fscore(y_true, y_pred):
    """ Calculate f-score with precision and recall scores
        Args:
            y_true: array, ground truth (correct) target values.
            y_pred: array, estimated targets as returned by a model.
        Returns:
            (precision, recall, fscore), evaluation scores """
    #
    TP = sum((y_true == 1)&(y_pred == 1))
    FP = sum((y_true == 1)&(y_pred == 0))
    FN = sum((y_true == 0)&(y_pred == 1))
    TN = sum((y_true == 0)&(y_pred == 0))
    #
    precision = TP/(TP+FP)
    recall    = TP/(TP+FN)
    accuracy  = (TP+TN)/(TP+TN+FP+FN)
    f1_score  = 2*(precision*recall)/(precision+recall)
    #
    res = (precision, recall, accuracy, f1_score)
    return res


def scoring (blocks, cards, top_n = 3):
    """ Evaluate model performace  
        Args:
            blocks: list, subgraph blocks
            cards: list, card set
        Return:
            list, result scores """
    #
    import numpy as np
    #
    cids, y_true = [], []
    for obj in cards:
        cids.append(obj[0])
        y_true.append(obj[-1])
    #
    y_pred = [0 for i in range(len(cids))] 
    for blk in blocks[:top_n]:
        for obj in blk['Nodes']['CreditCard']:
            y_pred[cids.index(obj[0])] = 1
    #
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    res = cal_precision_recall_fscore(y_true, y_pred)
    return res
