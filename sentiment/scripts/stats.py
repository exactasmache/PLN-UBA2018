"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
import os
from docopt import docopt
from collections import defaultdict

from sentiment.tass import InterTASSReader, GeneralTASSReader
import sentiment.configs as cfg
from collections import Counter

class TweetStats:
    """Several statistics for a Tweet corpus.
    """

    def __init__(self, tagged_sents):
        """
        tagged_sents -- corpus (list/iterable/generator of tagged sentences)
        """
        # WORK HERE!!
        # COLLECT REQUIRED STATISTICS INTO DICTIONARIES.

    

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    print('InterTASS train tweets')
    reader = InterTASSReader(cfg.InterTASS_train_path)
    tweets = list(reader.tweets())  # iterador sobre los tweets
    X = list(reader.X())  # iterador sobre los contenidos de los tweets
    y = list(reader.y())  # iterador sobre las polaridades de los tweets
    print('Total amount of tweets:', len(X))
    print(Counter(y))

    print('GeneralTASS train tweets')
    reader = GeneralTASSReader(cfg.GeneralTASS_train_path)
    tweets = list(reader.tweets())  # iterador sobre los tweets
    X = list(reader.X())  # iterador sobre los contenidos de los tweets
    y = list(reader.y())  # iterador sobre las polaridades de los tweets
    print('Total amount of tweets:', len(X))
    print(Counter(y))