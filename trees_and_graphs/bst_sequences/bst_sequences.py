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

    def dfs(self, node):
        if node is None:
            return []

        permutations = []
        for perm1 in self.dfs(node.left):
            for perm2 in self.dfs(node.right):
                permutations.append([node.value] + [perm1] + [perm2])
                permutations.append([node.value] + [perm2] + [perm1])
        if len(permutations) == 0:
            return [node.value]
        return permutations

    # FIX REPRESENTING ALGO
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


def build_tree(sorted_arr):
    if len(sorted_arr) == 0:
        return None
    mid_ind = len(sorted_arr) // 2
    root = Node(sorted_arr[mid_ind])
    root.left = build_tree(sorted_arr[:mid_ind])
    root.right = build_tree(sorted_arr[mid_ind+1:])
    return root


tree = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
