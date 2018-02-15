"""Train an n-gram model.

Usage:
  train.py [-m <model>] -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
                  inter: N-grams with interpolation smoothing.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import languagemodeling.config as cfg

from nltk.corpus import gutenberg, PlaintextCorpusReader
from collections import Counter

from languagemodeling.ngram import NGram
# from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram


# models = {
#     'ngram': NGram,
#     'addone': AddOneNGram,
#     'inter': InterpolatedNGram,
# }

from nltk.tokenize import RegexpTokenizer


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data:
    # we define a re to tokenize
    pattern = r'''(?x)    # set flag to allow verbose regexps
        (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
      | \w+(?:-\w+)*        # words with optional internal hyphens
      | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
      | \.\.\.            # ellipsis
      | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''
    tokenizer = RegexpTokenizer(pattern)

    chesterton_corpus = PlaintextCorpusReader(cfg.corpus_root, '.*\.txt', word_tokenizer=tokenizer)
    fileids = chesterton_corpus.fileids()

    # counter to do elemental statistics in order to test the tokenizer
    count = Counter()

    for sent in chesterton_corpus.sents():
      count.update(sent)

    print('10 palabras mas frecuentes:', count.most_common()[:10])
    print('Vocabulario:', len(count))
    print('Tokens:', sum(count.values()))

    exit()
    
    sents = chesterton_corpus.sents()
    
    # train the model
    n = int(opts['-n'])
    model = NGram(n, sents)
    # model_class = models[opts['-m']]
    # model = model_class(n, sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
