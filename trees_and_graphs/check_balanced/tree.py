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

    def max_depth(self, node):
        if node is None:
            return 0
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        if left_depth > right_depth:
            return 1 + left_depth
        return 1 + right_depth

    def is_balanced(self):
        tree_queue = collections.deque()
        tree_queue.append(self)
        while len(tree_queue) > 0:
            elem = tree_queue.popleft()
            max_size = self.visit(elem.left)
            left_size = self.visit(elem.right)
            if abs(max_size - left_size) > 1:
                return False
            if elem.left is not None:
                tree_queue.append(elem.left)
            if elem.right is not None:
                tree_queue.append(elem.right)
        return True

    def visit(self, node):
        return self.max_depth(node)

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
print(tree.is_balanced())
