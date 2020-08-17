import unittest
import string_rotation


class StringRotationTestCast(unittest.TestCase):
    def test_empty_string(self):
        str1 = ''
        str2 = ''
        self.assertEqual(
            string_rotation.is_rotation(str1, str2),
            True
        )

    def test_one_char_string(self):
        one_char_strings = [
            'a',
            'a',
        ]
        one_char_rotations = [
            'a',
            'b',
        ]
        answers = [
            True,
            False,
        ]
        self.rotation_test(one_char_strings, one_char_rotations, answers)

    def test_two_char_string(self):
        two_char_strings = [
            'ab',
            'ab',
            'ab',
        ]
        two_char_rotations = [
            'ba',
            'ab',
            'bc'
        ]
        answers = [
            True,
            True,
            False
        ]
        self.rotation_test(two_char_strings, two_char_rotations, answers)

    def test_three_char_string(self):
        three_char_strings = [
            'abc',
            'abc',
            'abc',
            'abc',
        ]
        three_char_rotations = [
            'cab',
            'bca',
            'abc',
            'ads',
        ]
        answers = [
            True,
            True,
            True,
            False,
        ]

    def test_other_string_size(self):
        str1 = 'a'
        str2 = 'asd'
        self.assertEqual(
            string_rotation.is_rotation(str1, str2),
            False
        )

    def rotation_test(self, strings, rotations, answers):
        for i, triple in enumerate(zip(strings, rotations, answers)):
            string, rotation, answer = triple
            with self.subTest(i=i):
                self.assertEqual(
                    string_rotation.is_rotation(string, rotation),
                    answer
                )
