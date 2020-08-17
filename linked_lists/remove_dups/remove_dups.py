class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


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

    def remove_dups(self, use_buffer=True):
        if use_buffer:
            self.__remove_dups_with_buffer()
        else:
            self.__remove_dups_without_buffer()

    def __remove_dups_with_buffer(self):
        unique_values = set()
        n = self.head

        while n is not None:
            unique_values.add(n.value)
            n = n.next_node

        for value in unique_values:
            self.remove(value, 2, True)

    def __remove_dups_without_buffer(self):
        n = self.head
        while n is not None:
            self.remove(n.value, 2, True)
            n = n.next_node

    def remove(self, value, begin_from=1, remove_all=False):
        counter = 0
        # Remove from the beginning
        while self.head.value == value:
            counter += 1
            if counter < begin_from:
                break
            self.head = self.head.next_node
            if not remove_all:
                return

        # Remove from the middle to the end
        n = self.head
        while n.next_node is not None:
            if n.next_node.value == value:
                counter += 1
                if counter < begin_from:
                    n = n.next_node
                    continue
                n.next_node = n.next_node.next_node
                if not remove_all:
                    return
                continue
            n = n.next_node

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