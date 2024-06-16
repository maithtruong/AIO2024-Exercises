'''
    1. Classification metrics (F1-Score).
'''

def precision(tp, fp):
    return tp / (tp + fp)

def recall(tp, fn):
    return tp / (tp + fn)

def f1_score(tp, fp, fn):
    prec = precision(tp, fp)
    rec = recall(tp, fn)
    return 2 * (prec * rec) / (prec + rec)

def metrics(tp, fp, fn):
    for metric in [tp, fp, fn]:
        if not isinstance(metric, int):
            print('All inputs must be integers!')
            return
        if metric < 0:
            print('All inputs must be greater than or equal to 0!')
            return
    
    prec = precision(tp, fp)
    rec = recall(tp, fn)
    f1 = f1_score(tp, fp, fn)

    print('Precision:', prec)
    print('Recall:', rec)
    print('F1-Score:', f1)
    
    return f1

def main():
    # Example
    print("Example 1:")
    metrics(tp=2, fp=3, fn=4)
    print("Example 2:")
    metrics(tp=-1, fp=3, fn=4)
    print("Example 3:")
    metrics(tp=2.5, fp=3, fn=4)

if __name__ == "__main__":
    main()