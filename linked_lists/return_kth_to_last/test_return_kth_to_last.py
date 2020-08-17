import unittest
import return_kth_to_last


class ReturnKthToLastTestCase(unittest.TestCase):
    def test_empty_list(self):
        linked_list = return_kth_to_last.LinkedList()
        answers = [
            None,
            None,
            None,
            None,
            None,
            None,
        ]
        self.return_kth_to_last_test(linked_list, answers)

    def test_one_elem_list(self):
        linked_list = return_kth_to_last.LinkedList(
            return_kth_to_last.Node(1),
        )
        answers = [
            return_kth_to_last.Node(1),
            None,
            None,
            None,
            None,
            None,
        ]
        self.return_kth_to_last_test(linked_list, answers)

    def test_two_elem_list(self):
        linked_list = return_kth_to_last.LinkedList(
            return_kth_to_last.Node(2,
            return_kth_to_last.Node(1))
        )
        answers = [
            return_kth_to_last.Node(1),
            return_kth_to_last.Node(2),
            None,
            None,
            None,
            None,
        ]
        self.return_kth_to_last_test(linked_list, answers)

    def test_three_elem_list(self):
        linked_list = return_kth_to_last.LinkedList(
            return_kth_to_last.Node(3,
            return_kth_to_last.Node(2,
            return_kth_to_last.Node(1)))
        )
        answers = [
            return_kth_to_last.Node(1),
            return_kth_to_last.Node(2),
            return_kth_to_last.Node(3),
            None,
            None,
            None,
        ]
        self.return_kth_to_last_test(linked_list, answers)

    def test_four_elem_list(self):
        linked_list = return_kth_to_last.LinkedList(
            return_kth_to_last.Node(4,
            return_kth_to_last.Node(3,
            return_kth_to_last.Node(2,
            return_kth_to_last.Node(1))))
        )
        answers = [
            return_kth_to_last.Node(1),
            return_kth_to_last.Node(2),
            return_kth_to_last.Node(3),
            return_kth_to_last.Node(4),
            None,
            None,
        ]
        self.return_kth_to_last_test(linked_list, answers)

    def return_kth_to_last_test(self, linked_list, answers):
        for i in range(6):
            with self.subTest(i=i):
                result = linked_list.return_kth_to_last(i)
                self.assertEqual(
                    result,
                    answers[i]
                )
