import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
                return
            self.right.insert(value)
        else:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
                return
            self.left.insert(value)

    def get_successor(self, node):
        if node.right is not None:
            return node.right

        if node.parent is None:
            return None

        next_node = node.parent
        while next_node.value < node.value:
            # just go up to the parent and get successor
            next_node = next_node.parent
            if next_node is None:
                return None
        return next_node

    # FIX REPRESENTING ALGO
    def __str__(self):
        return str(self.value)


def build_tree(sorted_arr):
    if len(sorted_arr) == 0:
        return None
    mid_ind = len(sorted_arr) // 2
    root = Node(sorted_arr[mid_ind])
    root.left = build_tree(sorted_arr[:mid_ind])
    root.right = build_tree(sorted_arr[mid_ind+1:])
    return root


tree = Node(5)
tree.insert(10)
tree.insert(11)
tree.insert(12)
tree.insert(4)

node = tree.left
while node is not None:
    print('NODE: {}'.format(node.value))
    node = tree.get_successor(node)
