# https://docs.python.org/3/library/unittest.html
from unittest import TestCase

from sentiment.classifier import SentimentClassifier, SentimentClassifier_tkn
import emoji
import re


class TestSentimentClassifier_tkn(TestCase):

    def setUp(self):
        self.emojis = set(emoji.UNICODE_EMOJI)
        self.x = '@Sakura_Abril Ow Bueno, no pasa nada, cuando puedas\
         confirmarlo, estoy aquí 😊 Y si no pudieras de cosplay pero sí a la expo, +'

    def test_basicClassifier(self):
        model = SentimentClassifier()

        res = ['sakura_abril', 'ow', 'bueno', 'no', 'pasa', 'nada', 'cuando',
               'puedas', 'confirmarlo', 'estoy', 'aquí', 'si', 'no', 'pudieras',
               'de', 'cosplay', 'pero', 'sí', 'la', 'expo']
        analyze = model.countvectorizer.build_analyzer()
        self.assertEqual(analyze(self.x), res)

    def test_tknClassifier(self):
        model = SentimentClassifier_tkn()

        res = ['@', 'sakura_abril', 'ow', 'bueno', ',', 'no', 'pasa', 'nada',
               ',', 'cuando', 'puedas', 'confirmarlo', ',', 'estoy', 'aquí',
               '😊', 'y', 'si', 'no', 'pudieras', 'de', 'cosplay', 'pero',
               'sí', 'a', 'la', 'expo', ',', '+']
        analyze = model.countvectorizer.build_analyzer()
        self.assertEqual(analyze(self.x), res)
