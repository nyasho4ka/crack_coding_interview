import collections


class Node:
    def __init__(self, value):
        self.value = value
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

    def is_subtree(self, subtree):
        subtree_nodes = self.bfs(subtree)
        print([node.value for node in subtree_nodes])
        for subtree_node in subtree_nodes:
            if self.is_sub(subtree_node, subtree):
                return True
        return False

    def is_sub(self, sub_node, subtree):
        first_queue = collections.deque()
        second_queue = collections.deque()

        node1 = sub_node
        node2 = subtree

        first_queue.append(node1)
        second_queue.append(node2)

        while len(first_queue) > 0 and len(first_queue) == len(second_queue):
            elem1 = first_queue.popleft()
            elem2 = second_queue.popleft()
            if elem1.value != elem2.value:
                return False
            if elem1.left is not None:
                first_queue.append(elem1.left)
            if elem1.right is not None:
                first_queue.append(elem1.right)
            if elem2.left is not None:
                second_queue.append(elem2.left)
            if elem2.right is not None:
                second_queue.append(elem2.right)
        return True

    def bfs(self, searched_node):
        node = self
        tree_queue = collections.deque()
        tree_queue.append(node)

        found_node_queue = collections.deque()
        while len(tree_queue) > 0:
            elem = tree_queue.popleft()
            if elem.value == searched_node.value:
                found_node_queue.append(elem)
            if elem.left is not None:
                tree_queue.append(elem.left)
            if elem.right is not None:
                tree_queue.append(elem.right)
        return found_node_queue

    def visit(self, node):
        pass


def build_tree(sorted_arr):
    if len(sorted_arr) == 0:
        return None
    mid_ind = len(sorted_arr) // 2
    root = Node(sorted_arr[mid_ind])
    root.left = build_tree(sorted_arr[:mid_ind])
    root.right = build_tree(sorted_arr[mid_ind+1:])
    return root


tree = build_tree([1, 2, 3])
tree2 = build_tree([1, 2, 3, 4, 5, 6])
print(tree2.is_subtree(tree))
