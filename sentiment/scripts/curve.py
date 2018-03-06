"""Draw a learning curve for a Sentiment Analysis model.

Usage:
  curve.py [-i <file>] [-m <model>] [-c <clf>]
  curve.py -h | --help

Options:
  -i <file>     Trained model file.
  -m <model>    Model to use if not input file given [default: basemf]:
                  basemf: Most frequent sentiment
                  clf: Machine Learning Classifier
  -c <clf>      Classifier to use if the model is a MEMM [default: svm]:
                  maxent: Maximum Entropy (i.e. Logistic Regression)
                  svm: Support Vector Machine
                  mnb: Multinomial Bayes
  -h --help     Show this screen.
"""
from docopt import docopt

from sentiment.tass import InterTASSReader, GeneralTASSReader
from sentiment.baselines import MostFrequent
from sentiment.classifier import SentimentClassifier
from sentiment.evaluator import Evaluator

import pickle
import os
import sentiment.configs as cfg
import numpy as np
import platform

if platform.system() == 'Darwin':
    import matplotlib
    matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


models = {
    'basemf': MostFrequent,
    'clf': SentimentClassifier,
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load training corpus
    reader1 = InterTASSReader(cfg.tweets['InterTASS']['train']['path'])
    X1, y1 = list(reader1.X()), list(reader1.y())
    reader2 = GeneralTASSReader(
        cfg.tweets['GeneralTASS']['train']['path'], simple=True)
    X2, y2 = list(reader2.X()), list(reader2.y())
    X, y = X1 + X2, y1 + y2

    # load development corpus (for evaluation)
    reader = InterTASSReader(cfg.tweets['InterTASS']['development']['path'])
    Xdev, y_true = list(reader.X()), list(reader.y())


    # load model if given
    if opts['-i']:
      filename = opts['-i']
      f = open(filename, 'rb')
      model = pickle.load(f)
      f.close()
      filename = os.path.basename(filename)

    else:
      # create model and evaluator instances
      # train model
      model_type = opts['-m']
      filename = ''
      if model_type == 'clf':
          model = models[model_type](clf=opts['-c'])
          filename += model.name() +'_'
          if not opts['-c']:
              filename += 'svm'
          else:
              filename += opts['-c']
      else:
          filename += 'basemf'
          model = models[model_type]()  # baseline


    evaluator = Evaluator()

    N = len(X)
    ns = []
    accs = []
    f1s = []
    for i in reversed(range(8)):
        n = int(N / 2**i)
        this_X = X[:n]
        this_y = y[:n]

        # train, test and evaluate
        model.fit(this_X, this_y)
        y_pred = model.predict(Xdev)
        evaluator.evaluate(y_true, y_pred)

        # print this data point:
        acc = evaluator.accuracy()
        f1 = evaluator.macro_f1()
        ns += [n]
        accs += [acc]
        f1s += [f1]
        print('n={}, acc={:2.2f}, f1={:2.2f}'.format(n, acc, f1))

    x = np.linspace(0, 10, 500)
    dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

    fig, ax = plt.subplots()
    line1, = ax.plot(ns, accs, linewidth=2, label='Accuracy')
    line2, = ax.plot(ns, f1s, linewidth=2, label='F1')

    if not os.path.exists(cfg.graphs_path):
        os.makedirs(cfg.graphs_path)

    filepath = os.path.join(cfg.graphs_path, filename+'.png')

    print('saving on \'{}\''.format(filepath))
    plt.savefig(filepath, bbox_inches='tight')
