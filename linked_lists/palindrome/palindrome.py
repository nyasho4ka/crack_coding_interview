"""
Suppose that in this task we have list size
and function return kth elem from last.
So we can easily implement function that
will calculate that the linked list is a palindrome
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.__str__() == other.__str__()


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.__get_tail()

    def __get_tail(self):
        if self.head is None:
            return None

        n = self.head
        while n.next_node is not None:
            n = n.next_node
        return n

    def return_kth_to_last(self, k):
        size = self.get_size()
        element_number = size - k - 1
        if element_number < 0:
            return None
        n = self.head
        for i in range(element_number):
            n = n.next_node
        return n

    def get_size(self):
        size = 0
        n = self.head
        while n is not None:
            size += 1
            n = n.next_node
        return size

    def is_palindrome(self):
        size = self.get_size()
        for i in range(size // 2):
            if self.return_kth_to_last(i) != self.return_kth_to_last(size - i - 1):
                return False
        return True

    def __str__(self):
        if self.head is None:
            return ''

        result = ''

        n = self.head
        while n is not None:
            result += str(n.value) + '->'
            n = n.next_node

        return result[:-2]

    def __eq__(self, other):
        return self.__str__() == other.__str__()