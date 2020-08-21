import unittest
from sum_lists import LinkedList, Node


class SumListsTestCase(unittest.TestCase):
    def test_one_plus_one(self):
        first = LinkedList(Node(1))
        second = LinkedList(Node(2))

        self.assertEqual(
            first+second,
            LinkedList(Node(3))
        )

    def test_two_plus_two(self):
        first = LinkedList(Node(1, Node(2)))
        second = LinkedList(Node(2, Node(3)))

        self.assertEqual(
            first+second,
            LinkedList(Node(3, Node(5)))
        )

    def test_three_plus_three(self):
        first = LinkedList(Node(1, Node(2, Node(3))))
        second = LinkedList(Node(5, Node(2, Node(7))))

        self.assertEqual(
            first+second,
            LinkedList(Node(6, Node(4, Node(0, Node(1)))))
        )

    def test_three_plus_one(self):
        first = LinkedList(Node(9, Node(9, Node(9))))
        second = LinkedList(Node(9))
        self.assertEqual(
            first+second,
            LinkedList(Node(8, Node(0, Node(0, Node(1)))))
        )
