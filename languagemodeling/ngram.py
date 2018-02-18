# https://docs.python.org/3/library/collections.html
from collections import defaultdict
import math

START = '<s>'
END = '</s>'


class LanguageModel(object):

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        return 0.0

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        return -math.inf

    def log_prob(self, sents):
        result = 0.0
        for _, sent in enumerate(sents):
            lp = self.sent_log_prob(sent)
            if lp == -math.inf:
                return lp
            result += lp
        return result

    def cross_entropy(self, sents):
        log_prob = self.log_prob(sents)
        n = sum(len(sent) + 1 for sent in sents)  # count '</s>' events
        e = - log_prob / n
        return e

    def perplexity(self, sents):
        return math.pow(2.0, self.cross_entropy(sents))


class NGram(LanguageModel):

    def generate_n_grams_count_dict_by_sent(self, n, sent, count, all=False):
        """
        n -- order of the model.
        sent -- list of tokens.
        count -- defaultdict of count of ngrams
        """
        r = range(0, n+1) if all else [n]
        for k in r:
            ksent = [START] * (k - 1) + sent + [END]
            top = len(ksent)
            for i in range(top - max(k, 1) + 1):
                kgram = tuple(ksent[i:i+k])
                count[kgram] += 1
                if not all:
                    count[kgram[:-1]] += 1

    def generate_n_grams_count_dict(self, n, sents, all=False):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        count = defaultdict(int)
        for sent in sents:
            self.generate_n_grams_count_dict_by_sent(n, sent, count, all)
        return dict(count)

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self._n = n
        self._count = self.generate_n_grams_count_dict(n, sents)

    def get_ngrams(self, lenght=None):
        return self._count.keys()

    def compute_vocabulary(self):
        voc = set([item for sublist in self.get_ngrams()
                   for item in sublist])
        voc.discard(START)
        return voc

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None, given_n=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        given_n -- allows
        """
        n = self._n if given_n == None else given_n
        print(n, len(prev_tokens))

        # if now prev_tokens, then prev_tokens=():
        prev_tokens = prev_tokens or ()
        assert len(prev_tokens) == n - 1

        # if string given, we convert it to a 1-uple:
        token = (token,) if isinstance(token, str) else token

        amount = self._count.get(prev_tokens, 0)
        if amount == 0:
            return 0.

        return self._count.get(prev_tokens+token, 0) / float(amount)

    def calculate_prob(self, sent, p_type='linear'):
        """Probability of a sentence given previous tokens and probability type.

          sent -- the sentence as a list of tokens.
          p_tokens -- the list of previous tokens.
          p_type -- the probability type to calculate.
        """
        res = 0 if p_type == 'log' else 1
        p_tokens = (START,) * (self._n-1)

        for token in sent+[END]:
            prob = self.cond_prob(token, p_tokens)
            if prob == 0:
                return float('-inf') if p_type == 'log' else 0
            res = res + math.log(prob, 2) if p_type == 'log' else res * prob
            p_tokens = (p_tokens + (token,))[1:]

        return res

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """

        return self.calculate_prob(sent)

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """

        return self.calculate_prob(sent, 'log')


class AddOneNGram(NGram):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        # call superclass to compute counts
        super().__init__(n, sents)

        # compute vocabulary
        self._voc = self.compute_vocabulary()
        self._V = len(self._voc)  # vocabulary size

    def V(self):
        """Size of the vocabulary.
        """
        return self._V

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        V = self._V
        # if prev_tokens not given, assume 0-uple:
        prev_tokens = prev_tokens or ()
        assert len(prev_tokens) == n - 1
        tokens = prev_tokens + (token,)
        return float(self.count(tokens) + 1) / float(self.count(prev_tokens) + V)


class InterpolatedNGram(NGram):

    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self._n = n

        if gamma is not None:
            # everything is training data
            train_sents = sents
        else:
            # 90% training, 10% held-out
            m = int(0.9 * len(sents))
            train_sents = sents[:m]
            held_out_sents = sents[m:]

        print('Computing counts...')
        # COMPUTE COUNTS FOR ALL K-GRAMS WITH K <= N
        self._count = self.generate_n_grams_count_dict(n, train_sents, True)

        # compute vocabulary size for add-one in the last step
        self._addone = addone
        if addone:
            print('Computing vocabulary...')
            self._voc = self.compute_vocabulary()
            self._V = len(self._voc)  # vocabulary size

        # compute gamma if not given
        if gamma is not None:
            self._gamma = gamma
        else:
            print('Computing gamma...')
            # use grid search to choose gamma
            min_gamma, min_p = None, float('inf')

            # WORK HERE!! TRY DIFFERENT VALUES BY HAND:
            for gamma in [100 + i * 50 for i in range(10)]:
                self._gamma = gamma
                p = self.perplexity(held_out_sents)
                print('  {} -> {}'.format(gamma, p))

                if p < min_p:
                    min_gamma, min_p = gamma, p

            print('  Choose gamma = {}'.format(min_gamma))
            self._gamma = min_gamma

    def count(self, tokens):
        """Count for an k-gram for k <= n.

        tokens -- the k-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        # if prev_tokens not given, assume 0-uple:
        prev_tokens = prev_tokens or ()
        assert len(prev_tokens) == n - 1

        gamma = self._gamma
        addone = self._addone

        prob = 0.0
        cum_lambda = 0.0  # sum of previous lambdas
        for i in range(n):
            # i-th term of the sum
            p_tkns = prev_tokens[i:]
            tokens = p_tkns + (token,)
            appear = self.count(tokens)
            t_amount = self.count(p_tkns)
            
            # COMPUTE lambdaa AND cond_ml.
            if i < n - 1:
                cond_ml = 0. if appear == 0 else appear / t_amount

                lambdaa = (1 - cum_lambda) * t_amount / \
                    (t_amount + gamma)
            else:
                # COMPUTE lambdaa AND cond_ml.
                if addone:
                    cond_ml = float(appear + 1) / t_amount + self._V
                else:
                    cond_ml = 0. if appear == 0 else appear / t_amount

                lambdaa = 1 - cum_lambda

            print(i, p_tkns, tokens, appear, t_amount, cond_ml, lambdaa)

            prob += lambdaa * cond_ml
            cum_lambda += lambdaa

        return prob