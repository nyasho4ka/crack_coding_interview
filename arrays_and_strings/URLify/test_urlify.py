import unittest
import urlify


class URLifyTestCase(object):
    def test_string_without_spaces(self):
        string = 'string_without_spaces'
        self.assertEqual(
            self.urlify(string, len(string)),
            list('string_without_spaces')
        )

    def test_string_with_one_space(self):
        string = 'one two  '
        self.assertEqual(
            self.urlify(string, len(string) - 2),
            ['o', 'n', 'e', '%', '2', '0', 't', 'w', 'o']
        )

    def test_string_with_two_spaces(self):
        string = 'one two three    '
        self.assertEqual(
            self.urlify(string, len(string) - 4),
            ['o', 'n', 'e', '%', '2', '0', 't', 'w', 'o', '%', '2', '0', 't', 'h', 'r', 'e', 'e']
        )

    def test_string_with_spaces_in_a_row(self):
        string = 'one  two  three        '
        self.assertEqual(
            self.urlify(string, len(string) - 8),
            ['o', 'n', 'e', '%', '2', '0', '%', '2', '0', 't', 'w', 'o', '%', '2', '0', '%', '2', '0', 't', 'h', 'r', 'e', 'e']
        )

    def test_empty_string(self):
        string = ''
        self.assertEqual(
            self.urlify(string, len(string)),
            []
        )

    def test_only_spaces_string(self):
        string = '      '
        self.assertEqual(
            self.urlify(string, len(string) - 4),
            ['%', '2', '0', '%', '2', '0']
        )


class URLifyV1TestCase(unittest.TestCase, URLifyTestCase):
    def setUp(self):
        self.urlify = urlify.urlify


class URLifyPITestCase(unittest.TestCase, URLifyTestCase):
    def setUp(self):
        self.urlify = urlify.urlify_pi
