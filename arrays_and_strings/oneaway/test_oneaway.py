import oneaway
import unittest


class OneAwayTestCase(unittest.TestCase):
    def setUp(self):
        self.ref_string = 'pale'
        self.empty_string = ''

        self.insert_one_end = 'pales'
        self.insert_one_start = 'opale'
        self.insert_one_middle = 'palle'

        self.remove_one_end = 'pal'
        self.remove_one_start = 'ale'
        self.remove_one_middle = 'ple'

        self.change_one_end = 'palo'
        self.change_one_start = 'hale'
        self.change_one_middle = 'pate'

        self.insert_two_end = 'paless'
        self.insert_two_start = 'oppale'
        self.insert_two_middle = 'papple'

        self.remove_two_end = 'pa'
        self.remove_two_start = 'le'
        self.remove_two_middle = 'pe'

        self.change_two_end = 'pack'
        self.change_two_start = 'tole'
        self.change_two_middle = 'puke'

    def testOneInsertEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_one_end),
            True
        )

    def testOneInsertBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_one_start),
            True
        )

    def testOneInsertMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_one_middle),
            True
        )

    def testOneRemoveEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_one_end),
            True
        )

    def testOneRemoveBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_one_start),
            True
        )

    def testOneRemoveMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_one_middle),
            True
        )

    def testOneChangeEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_one_end),
            True
        )

    def testOneChangeBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_one_start),
            True
        )

    def testOneChangeMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_one_middle),
            True
        )

    def testEmptyAndFull(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.empty_string),
            False
        )

    def testEmptyAndEmpty(self):
        self.assertEqual(
            oneaway.oneaway(self.empty_string, self.empty_string),
            True
        )

    def testTwoInsertEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_two_end),
            False
        )

    def testTwoInsertBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_two_start),
            False
        )

    def testTwoInsertMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.insert_two_middle),
            False
        )

    def testTwoRemoveEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_two_end),
            False
        )

    def testTwoRemoveBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_two_end),
            False
        )

    def testTwoRemoveMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.remove_two_middle),
            False
        )

    def testTwoChangesEnd(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_two_end),
            False
        )

    def testTwoChangesBegin(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_two_start),
            False
        )

    def testTwoChangesMiddle(self):
        self.assertEqual(
            oneaway.oneaway(self.ref_string, self.change_two_middle),
            False
        )
