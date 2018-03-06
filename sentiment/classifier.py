from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from nltk import word_tokenize
import emoji
from nltk.corpus import stopwords

classifiers = {
    'maxent': LogisticRegression,
    'mnb': MultinomialNB,
    'svm': LinearSVC,
}


class SentimentClassifier(object):

    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        self.countvectorizer = CountVectorizer()
        self._pipeline = Pipeline([
            ('vect', self.countvectorizer),
            ('clf', classifiers[clf]()),
        ])
    def name(self):
        return 'clf_basic'

    def fit(self, X, y):
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)


class SentimentClassifier_tkn(SentimentClassifier):
    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        self.countvectorizer = CountVectorizer(tokenizer=word_tokenize)
        self._pipeline = Pipeline([
            ('vect', self.countvectorizer),
            ('clf', classifiers[clf]()),
        ])

    def name(self):
      return 'clf_better_tokenizer'

class SentimentClassifier_binary(SentimentClassifier):
    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        self.countvectorizer = CountVectorizer(binary=True)
        self._pipeline = Pipeline([
            ('vect', self.countvectorizer),
            ('clf', classifiers[clf]()),
        ])

    def name(self):
      return 'clf_binary'

class SentimentClassifier_StopWords(SentimentClassifier):
    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        self.countvectorizer = CountVectorizer(stop_words=stopwords.words('spanish'))
        self._pipeline = Pipeline([
            ('vect', self.countvectorizer),
            ('clf', classifiers[clf]()),
        ])

    def name(self):
      return 'clf_binary'


ENG_NEGATE = { "aint", "arent", "cannot", "cant", "couldnt", "darent", "didnt", "doesnt",
 "ain't", "aren't", "can't", "couldn't", "daren't", "didn't", "doesn't",
 "dont", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt", "neither",
 "don't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't",
 "neednt", "needn't", "never", "none", "nope", "nor", "not", "nothing", "nowhere",
 "oughtnt", "shant", "shouldnt", "uhuh", "wasnt", "werent",
 "oughtn't", "shan't", "shouldn't", "uh-uh", "wasn't", "weren't",
 "without", "wont", "wouldnt", "won't", "wouldn't", "rarely", "seldom", "despite" }

SPANISH_NEGATE = {'no', 'tampoco', 'nunca', 'jamas'}

def add_negations(x):
    tokens = x.split()
    new_tokens = []
    negate = False
    for token in tokens:
        if token.lower() in SPANISH_NEGATE:
            negate = True
        elif token == '.':
            negate = False
        elif negate:
            token = 'NOT_' + token
        new_tokens.append(token)

    return ' '.join(new_tokens)


class SentimentClassifier_Negation(SentimentClassifier):
    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        self.countvectorizer = CountVectorizer(preprocessor=add_negations)
        self._pipeline = Pipeline([
            ('vect', self.countvectorizer),
            ('clf', classifiers[clf]()),
        ])

    def name(self):
      return 'clf_binary'