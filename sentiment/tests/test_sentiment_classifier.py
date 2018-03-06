# https://docs.python.org/3/library/unittest.html
from unittest import TestCase

from sentiment.classifier import (SentimentClassifier, SentimentClassifier_tkn,
                                  SentimentClassifier_binary, SentimentClassifier_StopWords,
                                  SentimentClassifier_Negation)
import re
from nltk.corpus import stopwords


class TestSentimentClassifier_tkn(TestCase):

    def setUp(self):
        self.emojiSent = '@Sakura_Abril Ow Bueno, no pasa nada, cuando puedas\
         confirmarlo, estoy aquí 😊 Y si no pudieras de cosplay pero sí a la expo, +'


    def test_basicClassifier(self):
        model = SentimentClassifier()

        res = ['sakura_abril', 'ow', 'bueno', 'no', 'pasa', 'nada', 'cuando',
               'puedas', 'confirmarlo', 'estoy', 'aquí', 'si', 'no', 'pudieras',
               'de', 'cosplay', 'pero', 'sí', 'la', 'expo']
        analyze = model.countvectorizer.build_analyzer()
        self.assertEqual(analyze(self.emojiSent), res)


    def test_tknClassifier(self):
        model = SentimentClassifier_tkn()

        res = ['@', 'sakura_abril', 'ow', 'bueno', ',', 'no', 'pasa', 'nada',
               ',', 'cuando', 'puedas', 'confirmarlo', ',', 'estoy', 'aquí',
               '😊', 'y', 'si', 'no', 'pudieras', 'de', 'cosplay', 'pero',
               'sí', 'a', 'la', 'expo', ',', '+']
        analyze = model.countvectorizer.build_analyzer()
        self.assertEqual(analyze(self.emojiSent), res)


    def test_stopWordsClassifier(self):
        model = SentimentClassifier_StopWords()
        stop_words = model.countvectorizer.get_stop_words()
        self.assertEqual(set(stopwords.words('spanish')), stop_words)


    def test_segativeWordsClassifier(self):
        sents = ['las tengo pero aún no las he leído . Caerán prontito',
                 'este verano tampoco ha llegado a hacer calor, \
                sobre todo si lo comparamos con el pasado']

        results = ['las tengo pero aún no NOT_las NOT_he NOT_leído . Caerán prontito',
                   'este verano tampoco NOT_ha NOT_llegado NOT_a NOT_hacer NOT_calor, \
                   NOT_sobre NOT_todo NOT_si NOT_lo NOT_comparamos NOT_con NOT_el NOT_pasado']
        
        model = SentimentClassifier_Negation()
        add_negations = model.countvectorizer.build_preprocessor()

        for i in range(len(sents)):
          self.assertEqual(add_negations(sents[i]), ' '.join(results[i].split()))