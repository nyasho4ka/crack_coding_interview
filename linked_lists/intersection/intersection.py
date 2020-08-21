class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def is_equal_by_address(self, other):
        return id(self) == id(other)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.__get_tail()
        self.size = None

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

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next_node

    def get_size(self):
        if self.size is None:
            counter = 0
            node = self.head
            while node is not None:
                counter += 1
                node = node.next_node
            self.size = counter
        return self.size


def is_intersected(list1, list2):
    """
    Get the linked lists sizes
    If list1 size > list2 size that iterate over list1 to get the same length
    Than iterate pair of elements and compare them elements
    LOGIC IS IF TWO LISTS HAVE INTERSECTION THAN ALL ELEMENTS
    AFTER THESE INTERSECTION ARE EQUAL
    """
    list1_size = list1.get_size()
    list2_size = list2.get_size()
    size_diff = list1_size - list2_size
    comp_elem1 = None
    comp_elem2 = None

    if size_diff > 0:
        counter = list2_size
        comp_elem2 = list2.head
        for i, el1 in enumerate(list1):
            if i == size_diff:
                comp_elem1 = el1
                break
    elif size_diff < 0:
        counter = list1_size
        comp_elem1 = list1.head
        for i, el2 in enumerate(list2):
            if i == abs(size_diff):
                comp_elem2 = el2
                break
    else:
        counter = list1_size
        comp_elem1 = list1.head
        comp_elem2 = list2.head

    for i in range(counter):
        if comp_elem1.is_equal_by_address(comp_elem2):
            return True
        comp_elem1 = comp_elem1.next_node
        comp_elem2 = comp_elem2.next_node
    return False
