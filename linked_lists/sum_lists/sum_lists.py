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

    def __add__(self, other):
        value = self.__get_sum(self.head) + other.__get_sum(other.head)
        result_linked = self.__get_list_by_value(value)
        return result_linked

    def __get_sum(self, node, order=1):
        if node.next_node is None:
            return node.value * order
        return node.value * order + self.__get_sum(node.next_node, order*10)

    def __get_list_by_value(self, value):
        if value < 10:
            return LinkedList(Node(value))
        head = LinkedList(Node(value % 10))
        n = head
        value /= 10
        while value > 0:
            next_node = Node(value % 10)
            n.next_node = next_node
            n = n.next_node
        return LinkedList(head)
