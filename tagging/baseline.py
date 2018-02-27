from collections import defaultdict


class BadBaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        pass

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return 'nc0s000'

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True


class BaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words.
        """
        self._default_tag = default_tag

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

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        if self.unknown(w):
          return self._default_tag 
        
        tags_dict = self._word_tag_dict[w]
        return sorted(tags_dict.items(), key=lambda t: t[1], reverse=True)[0][0]

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w not in self._word_tag_dict.keys()
