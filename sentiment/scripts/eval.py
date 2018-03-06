"""Evaulate a Sentiment Analysis model.

Usage:
  eval.py -i <file> [-f] [-d]
  eval.py -h | --help

Options:
  -i <file>     Trained model file.
  -f --final    Use final test set instead of development.
  -d --deep     Deep analysis (just with maxent)
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
from pprint import pprint
from collections import defaultdict

from sentiment.evaluator import Evaluator

import sentiment.configs as cfg
from sentiment.analysis import (
    print_maxent_features, print_feature_weights_for_item)

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load model
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    reader_class = cfg.tweets['InterTASS']['reader']
    # load corpus
    if not opts['--final']:
        reader = reader_class(cfg.tweets['InterTASS']['development']['path'])
    else:
        reader = reader_class(
            cfg.tweets['InterTASS']['test']['path'],
            cfg.tweets['InterTASS']['test']['res_path']
        )
    X, y_true = list(reader.X()), list(reader.y())

    # classify
    y_pred = model.predict(X)

    # evaluate and print
    evaluator = Evaluator()
    evaluator.evaluate(y_true, y_pred)
    evaluator.print_results()
    evaluator.print_confusion_matrix()
    
    # print (model)
    # for x,y,z in zip(X, y_pred, y_true):
    #   print (x, y, z)

    # detailed confusion matrix, for result analysis
    cm_items = defaultdict(list)
    for i, (true, pred) in enumerate(zip(y_true, y_pred)):
        cm_items[true, pred] += [i]

    if opts['--deep']:

        pipeline = model._pipeline
        vect = pipeline.named_steps['vect']
        clf = pipeline.named_steps['clf']

        print_maxent_features(vect, clf)

        X2 = [X[i] for i in cm_items['N', 'P']]
        # calculo las probabilidades para todas las clases
        P = pipeline.predict_proba(X2)
        delta = P[:, 3] - P[:, 0]  # diferencia entre prob de P y prob de N
        # ordeno de mayor a menor
        sorted_X2 = sorted(zip(X2, delta), key=lambda x: x[1], reverse=True)
        x = sorted_X2[0][0]
        print_feature_weights_for_item(vect, clf, x)
