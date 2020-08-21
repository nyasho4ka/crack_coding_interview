import unittest
import three_in_one


class ThreeInOneTestCase(unittest.TestCase):
    def test_empty_stacks(self):
        three = three_in_one.ThreeStacks(0, 0, 0)

        self.assertRaises(
            Exception,
            three.push
        )

    def test_one_size_stacks(self):
        three = three_in_one.ThreeStacks(1, 1, 1)
        three.push(1, 2)
        three.push(2, 3)
        three.push(3, 1)
        self.assertEqual(
            three,
            [2, 3, 1]
        )

    def test_two_size_stacks(self):
        three = three_in_one.ThreeStacks(2, 2, 2)
        three.push(1, 2)
        three.push(1, 10)
        three.push(2, 3)
        three.pop(2)
        three.push(3, 4)
        three.push(3, 5)
        three.push(2, 10)
        self.assertEqual(
            three,
            [2, 10, 10, None, 4, 5]
        )
