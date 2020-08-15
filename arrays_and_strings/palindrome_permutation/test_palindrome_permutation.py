import unittest
import palindrome_permutation


class PalindromePermutationTestCase(object):
    def test_palindrome_string(self):
        palindrome_string = 'Tact coa'
        self.assertEqual(
            self.palindrome_permutation(palindrome_string),
            True
        )

    def test_non_palindrome_string(self):
        non_palindrome_string = 'opppaa'
        self.assertEqual(
            self.palindrome_permutation(non_palindrome_string),
            False
        )

    def test_empty_string(self):
        empty_string = ''
        self.assertEqual(
            self.palindrome_permutation(empty_string),
            True
        )

    def test_one_char_string(self):
        one_char_string = 'o'
        self.assertEqual(
            self.palindrome_permutation(one_char_string),
            True
        )

    def test_with_many_spaces(self):
        many_spaces_string = 'aa s jj k sk lpo opl'
        self.assertEqual(
            self.palindrome_permutation(many_spaces_string),
            True
            )


class PalindromePermutationV1TestCase(unittest.TestCase, PalindromePermutationTestCase):
    def setUp(self):
        self.palindrome_permutation = palindrome_permutation.palindrome_permutation


class PalindromePermutationPITestCase(unittest.TestCase, PalindromePermutationTestCase):
    def setUp(self):
        self.palindrome_permutation = palindrome_permutation.palindrome_permutation_pi
