import is_unique
import unittest


class IsUniqueTestCase(object):
    def test_unique_string(self):
        unique_string = 'abcde'
        self.assertEqual(self.is_unique(unique_string), True)

    def test_non_unique_string(self):
        non_unique_string = 'aabbccee'
        self.assertEqual(self.is_unique(non_unique_string), False)

    def test_empty_string(self):
        empty_string = ''
        self.assertEqual(self.is_unique(empty_string), True)

    def test_one_char_string(self):
        one_char_string = 'f'
        self.assertEqual(self.is_unique(one_char_string), True)

    def test_extremely_string(self):
        extremely_string = 'abcdefghjzxva'
        self.assertEqual(self.is_unique(extremely_string), False)


class IsUniqueV1TestCase(unittest.TestCase, IsUniqueTestCase):
    def setUp(self):
        self.is_unique = is_unique.is_unique_v1


class IsUniqueV2TestCase(unittest.TestCase, IsUniqueTestCase):
    def setUp(self):
        self.is_unique = is_unique.is_unique_v2


class IsUniquePITestCase(unittest.TestCase, IsUniqueTestCase):
    def setUp(self):
        self.is_unique = is_unique.is_unique_pi
