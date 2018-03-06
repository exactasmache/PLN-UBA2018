"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
import os
from docopt import docopt

import sentiment.configs as cfg
from collections import Counter

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    t_type = 'train'
    for t in cfg.tweets.values():
        print(t[t_type]['name'])
        reader = t['reader'](t[t_type]['path'])
        tweets = list(reader.tweets())  # iterador sobre los tweets
        X = list(reader.X())  # iterador sobre los contenidos de los tweets
        y = list(reader.y())  # iterador sobre las polaridades de los tweets
        print('Total amount of tweets:', len(X))
        print(Counter(y))
