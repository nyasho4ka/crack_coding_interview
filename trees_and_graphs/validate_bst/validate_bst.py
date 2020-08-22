import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.length = 0
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
                return
            self.right.insert(value)
        else:
            if self.left is None:
                self.left = Node(value)
                return
            self.left.insert(value)

    def is_bst(self):
        if self is None:
            return
        left_max = self.get_max(self.left)
        right_min = self.get_min(self.right)
        print(left_max)
        print(right_min)
        print(self.value)
        return left_max <= self.value < right_min

    def get_max(self, node):
        if node is None:
            return 0

        left_max = self.get_max(node.left)
        right_max = self.get_max(node.right)

        return max(node.value, left_max, right_max)

    def get_min(self, node):
        if node is None:
            return float('inf')

        left_min = self.get_min(node.left)
        right_min = self.get_min(node.right)

        return min(node.value, left_min, right_min)

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
print(tree.is_bst())
