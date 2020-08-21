class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def is_equal(self, other, by_addr=True):
        if by_addr:
            return id(other) == id(self)
        return self == other

    def __hash__(self):
        return self.value


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

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

    def detect_loop(self):
        """
        We will use hash table 0(n) space and O(n) time complexity
        :return:
        """
        node_hash = dict()
        for node in self:
            if node in node_hash:
                return node
            node_hash[node] = 1

    def detect_loop_with_runner(self):
        """
        Runner technic with O(1) space and O(n) time complexity
        :return:
        """
        basic_node = self.head
        runner_node = self.head.next_node

        loop_size = 0
        # Check if there is a loop
        counter = 0
        while True:
            if basic_node.is_equal(runner_node):
                counter += 1
                loop_size = counter
                break
            basic_node = basic_node.next_node
            try:
                runner_node = runner_node.next_node.next_node
            except ValueError:
                break
            counter += 1

        return loop_size


nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
head = nodes[0]
head.next_node = nodes[1]
head.next_node.next_node = nodes[2]
head.next_node.next_node.next_node = nodes[3]
head.next_node.next_node.next_node.next_node = nodes[4]
head.next_node.next_node.next_node.next_node.next_node = nodes[2]

looped_list = LinkedList(head)
print(looped_list.detect_loop())
print(looped_list.detect_loop_with_runner())
