import unittest
import string_compression


class StringCompressionTestCase(unittest.TestCase):
    def testEmptyString(self):
        empty = ''
        self.assertEqual(
            string_compression.string_compression(empty),
            ''
        )

    def oneCharString(self):
        one_char_string = 'a'
        self.assertEqual(
            string_compression.string_compression(one_char_string),
            'a'
        )

    def testSingleStrings(self):
        strings = [
            'abcde',
            'dsert',
            'popopo'
        ]

        for i, word in enumerate(strings):
            with self.subTest(i=i):
                self.assertEqual(
                    string_compression.string_compression(word),
                    word
                )

    def testDoubleStrings(self):
        strings = [
            'aabbccdd',
            'ggssaass',
            'ppaallaaqqaa',
        ]

        for i, word in enumerate(strings):
            with self.subTest(i=i):
                self.assertEqual(
                    string_compression.string_compression(word),
                    word
                )

    def testOtherStrings(self):
        strings = [
            'aaabbcccc',
            'aabbccaaa',
            'popsocketooo',
            'oooopaaps',
            'aaaaa'
        ]

        result_strings = [
            'a3b2c4',
            'a2b2c2a3',
            'popsocketooo',
            'oooopaaps',
            'a5'
        ]

        for i, word in enumerate(strings):
            with self.subTest(i=i):
                self.assertEqual(
                    string_compression.string_compression(word),
                    result_strings[i]
                )
