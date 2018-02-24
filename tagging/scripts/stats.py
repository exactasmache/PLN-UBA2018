"""Print corpus statistics.

Usage:
  stats.py [-c <corpus>]
  stats.py -h | --help

Options:
  -h --help     Show this screen.
  -c <c>        Corpus path (if needed).
"""
import os
from docopt import docopt
from collections import defaultdict

import tagging.configs as cfg
from ancora import SimpleAncoraCorpusReader


class POSStats:
    """Several statistics for a POS tagged corpus.
    """

    def __init__(self, tagged_sents):
        """
        tagged_sents -- corpus (list/iterable/generator of tagged sentences)
        """
        self._sent_count = 0    # |sents|
        self._token_count = 0   # |tokens|

        # {D: {w1: 1, w4: 1}, ..., P: {w2: 2}},
        self._tag_word_dict = defaultdict(lambda: defaultdict(int))

        # {w1: {V: 1, A: 2}, ..., wn: {N: 4}}
        self._word_tag_dict = defaultdict(lambda: defaultdict(int))

        for sent in tagged_sents:
            self._sent_count += 1
            for word, tag in sent:
                self._token_count += 1
                self._word_tag_dict[word][tag] += 1
                self._tag_word_dict[tag][word] += 1

    def sent_count(self):
        """Total number of sentences."""
        return self._sent_count

    def token_count(self):
        """Total number of tokens."""
        return self._token_count

    def words(self):
        """Vocabulary (set of words)."""
        return self._word_tag_dict.keys()

    def word_count(self):
        """Vocabulary size."""
        return len(self._word_tag_dict)

    def word_freq(self, w):
        """Frequency of word w."""
        return sum([count for tag, count in self._word_tag_dict[w].items()])

    def unambiguous_words(self):
        """List of words with only one observed POS tag."""
        return self.ambiguous_words(1)

    def ambiguous_words(self, n):
        """List of words with n different observed POS tags.

        n -- number of tags.
        """
        return [w for w, tag in self._word_tag_dict.items() if len(tag) == n]

    def tags(self):
        """POS Tagset."""
        return self._tag_word_dict.keys()

    def tag_count(self):
        """POS tagset size."""
        return len(self.tags())

    def tag_freq(self, t):
        """Frequency of tag t."""
        return sum([count for word, count in self._tag_word_dict[t].items()])

    def tag_word_dict(self, t):
        """Dictionary of words and their counts for tag t."""
        return dict(self._tag_word_dict[t])


if __name__ == '__main__':
    opts = docopt(__doc__)

    c_path = opts['-c']
    c_path, df = (cfg.ancora_path, ' default') if not c_path else (c_path, '')

    log = "Using the{} corpus {}".format(
        df, os.path.basename(c_path.rstrip('/')))

    print(log)
    print('='*len(log))

    # load the data
    corpus = SimpleAncoraCorpusReader(c_path)
    sents = corpus.tagged_sents()

    # compute the statistics
    stats = POSStats(sents)

    print('Basic Statistics')
    print('================')
    print('sents: {}'.format(stats.sent_count()))
    token_count = stats.token_count()
    print('tokens: {}'.format(token_count))
    word_count = stats.word_count()
    print('words: {}'.format(word_count))
    print('tags: {}'.format(stats.tag_count()))
    print('')

    print('Most Frequent POS Tags')
    print('======================')
    tags = [(t, stats.tag_freq(t)) for t in stats.tags()]
    sorted_tags = sorted(tags, key=lambda t_f: -t_f[1])
    print('tag\tfreq\t%\ttop')
    for t, f in sorted_tags[:10]:
        words = stats.tag_word_dict(t).items()
        sorted_words = sorted(words, key=lambda w_f: -w_f[1])
        top = [w for w, _ in sorted_words[:5]]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(
            t, f, f * 100 / token_count, ', '.join(top)))
    print('')

    print('Word Ambiguity Levels')
    print('=====================')
    print('n\twords\t%\ttop')
    for n in range(1, 10):
        words = list(stats.ambiguous_words(n))
        m = len(words)

        # most frequent words:
        sorted_words = sorted(words, key=lambda w: -stats.word_freq(w))
        top = sorted_words[:5]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(
            n, m, m * 100 / word_count, ', '.join(top)))
