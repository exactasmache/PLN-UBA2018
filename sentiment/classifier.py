from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from nltk import word_tokenize
import emoji
emojis = set(emoji.UNICODE_EMOJI)

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

    