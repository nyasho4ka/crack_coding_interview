import check_permutation
import unittest


class CheckPermutationTestCase(object):
    def test_both_perms(self):
        first_string = 'abcba'
        second_string = 'bacab'
        self.assertEqual(
            self.check_permutation(first_string, second_string),
            True
        )

    def test_other_length(self):
        first_string = 'aaa'
        second_string = 'aa'
        self.assertEqual(
            self.check_permutation(first_string, second_string),
            False
        )

    def test_not_perms(self):
        first_string = 'abcde'
        second_string = 'fcdas'
        self.assertEqual(
            self.check_permutation(first_string, second_string),
            False
        )

    def test_empty_perms(self):
        first_string = ''
        second_string = ''
        self.assertEqual(
            self.check_permutation(first_string, second_string),
            True
        )

    def test_empty_and_not(self):
        first_string = ''
        second_string = 'asdasdsada'
        self.assertEqual(
            self.check_permutation(first_string, second_string),
            False
        )


class CheckPermutationV1TestCase(unittest.TestCase, CheckPermutationTestCase):
    def setUp(self):
        self.check_permutation = check_permutation.check_permutation


class CheckPermutationPITestCase(unittest.TestCase, CheckPermutationTestCase):
    def setUp(self):
        self.check_permutation = check_permutation.check_permutation_pi
