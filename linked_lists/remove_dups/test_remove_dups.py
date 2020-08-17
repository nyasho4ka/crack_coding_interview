import remove_dups
import unittest


class RemoveDupsTestCase(unittest.TestCase):
    def test_empty_linked_list(self):
        empty_list = remove_dups.LinkedList()
        result = remove_dups.LinkedList()
        empty_list.remove_dups(False)
        self.assertEqual(
            empty_list,
            result
        )

    def test_dups_in_begin(self):
        linked_list = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3))))
        )
        result = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        linked_list.remove_dups(False)
        self.assertEqual(
            linked_list,
            result
        )

    def test_dups_in_middle(self):
        linked_list = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(2, remove_dups.Node(3))))
        )
        result = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        linked_list.remove_dups(False)
        self.assertEqual(
            linked_list,
            result
        )

    def test_dups_in_end(self):
        linked_list = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3, remove_dups.Node(3))))
        )
        result = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        linked_list.remove_dups(False)
        self.assertEqual(
            linked_list,
            result
        )

    def test_dups_everywhere(self):
        linked_list = remove_dups.LinkedList(
            remove_dups.Node(1,
            remove_dups.Node(1,
            remove_dups.Node(2,
            remove_dups.Node(2,
            remove_dups.Node(3,
            remove_dups.Node(3))))))
        )
        result = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        linked_list.remove_dups(False)
        self.assertEqual(
            linked_list,
            result
        )

    def test_without_dups(self):
        linked_list = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        result = remove_dups.LinkedList(
            remove_dups.Node(1, remove_dups.Node(2, remove_dups.Node(3)))
        )
        linked_list.remove_dups(False)
        self.assertEqual(
            linked_list,
            result
        )
