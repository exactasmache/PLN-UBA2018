from collections import defaultdict
import random


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = model._n

        # compute the probabilities
        probs = defaultdict(dict)

        ngrams = list(model.get_ngrams())+[()]

        for ngram in ngrams:
            if len(ngram) == self._n:
                tkn, p_tkn = ngram[-1], ngram[:-1]
                p = model.cond_prob(tkn, p_tkn)
                probs[p_tkn][tkn] = p

        self._probs = dict(probs)

        # sort in descending order for efficient sampling
        # self._sorted_probs = {k: sorted(v.items()) for k, v in self._probs.items()}
        self._sorted_probs = {k: sorted(v.items(), key=lambda t: t[1]) 
          for k, v in self._probs.items()}
        
        print (self._sorted_probs)

    def generate_sent(self):
        """Randomly generate a sentence."""
        n = self._n

        sent = []
        prev_tokens = ['<s>'] * (n - 1)
        token = self.generate_token(tuple(prev_tokens))
        while token != '</s>':
                # WORK HERE!!
            pass

        return sent

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        r = random.random()
        probs = self._sorted_probs[prev_tokens]
        # WORK HERE!!

        return token
