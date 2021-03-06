# https://docs.python.org/3/library/unittest.html
from unittest import TestCase

from languagemodeling.ngram import NGram
from languagemodeling.ngram_generator import NGramGenerator


class TestNGramGenerator(TestCase):

    def setUp(self):
        self.sents = [
            'el gato come pescado .'.split(),
            'la gata come salmón .'.split(),
        ]
        self.total = 12.

    def test_init_1gram(self):
        ngram = NGram(1, self.sents)
        generator = NGramGenerator(ngram)

        probs = {
            (): {
                'el': 1 / self.total,
                'gato': 1 / self.total,
                'come': 2 / self.total,
                'pescado': 1 / self.total,
                '.': 2 / self.total,
                '</s>': 2 / self.total,
                'la': 1 / self.total,
                'gata': 1 / self.total,
                'salmón': 1 / self.total,
            }
        }

        self.assertEqual(generator._probs, probs)

    def test_init_2gram(self):
        ngram = NGram(2, self.sents)
        generator = NGramGenerator(ngram)

        probs = {
            ('<s>',): {'el': 0.5, 'la': 0.5},
            ('el',): {'gato': 1.0},
            ('gato',): {'come': 1.0},
            ('come',): {'pescado': 0.5, 'salmón': 0.5},
            ('pescado',): {'.': 1.0},
            ('.',): {'</s>': 1.0},
            ('la',): {'gata': 1.0},
            ('gata',): {'come': 1.0},
            ('salmón',): {'.': 1.0},
        }
        sorted_probs = {
            ('<s>',): [('el', 0.5), ('la', 0.5)],
            ('el',): [('gato', 1.0)],
            ('gato',): [('come', 1.0)],
            ('come',): [('pescado', 0.5), ('salmón', 0.5)],
            ('pescado',): [('.', 1.0)],
            ('.',): [('</s>', 1.0)],
            ('la',): [('gata', 1.0)],
            ('gata',): [('come', 1.0)],
            ('salmón',): [('.', 1.0)],
        }

        self.assertEqual(generator._probs, probs)
        self.assertEqual(generator._sorted_probs, sorted_probs)

    def test_generate_token(self):
        ngram = NGram(2, self.sents)
        generator = NGramGenerator(ngram)

        for _ in range(100):
            # after 'el' always comes 'gato':
            token = generator.generate_token(('el',))
            self.assertEqual(token, 'gato')

            # after 'come' may come 'pescado' or 'salmón'
            token = generator.generate_token(('come',))
            self.assertTrue(token in ['pescado', 'salmón'])

    def test_generate_sent_1gram(self):
        ngram = NGram(1, self.sents)
        generator = NGramGenerator(ngram)

        voc = {'<s>', 'el', 'gato', 'come', 'pescado',
               '.', 'la', 'gata', 'salmón', '</s>'}

        for _ in range(100):
            sent = generator.generate_sent()
            self.assertTrue(set(sent).issubset(voc))

    def test_generate_sent_2gram(self):
        ngram = NGram(2, self.sents)
        generator = NGramGenerator(ngram)

        # all the possible generated sentences for 2-grams:
        sents = [
            'el gato come pescado .',
            'la gata come salmón .',
            'el gato come salmón .',
            'la gata come pescado .',
        ]

        for _ in range(100):
            sent = generator.generate_sent()
            self.assertTrue(' '.join(sent) in sents, sent)
