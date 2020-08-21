import unittest
from intersection import *


class IntersectionTestCase(unittest.TestCase):
    def test_with_intersection_node(self):
        intersection_node = Node(5, Node(2, Node(7)))
        list1 = LinkedList(Node(1, Node(2, Node(3, intersection_node))))
        list2 = LinkedList(Node(2, Node(4, Node(123, Node(999, Node(0, intersection_node))))))
        self.assertEqual(
            is_intersected(list1, list2),
            True
        )

    def test_without_intersection_node(self):
        list1 = LinkedList(Node(1, Node(2, Node(3))))
        list2 = LinkedList(Node(1, Node(2, Node(3))))
        self.assertEqual(
            is_intersected(list1, list2),
            False
        )
