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

    # FIX REPRESENTING ALGO
    def __str__(self):
        return 'null'


def build_tree(sorted_arr):
    if len(sorted_arr) == 0:
        return None
    mid_ind = len(sorted_arr) // 2
    print("Mid index: {}".format(mid_ind))
    root = Node(sorted_arr[mid_ind])
    print("Middle value: {}".format(root.value))
    print('ENTER TO LEFT BRANCH')
    root.left = build_tree(sorted_arr[:mid_ind])
    print('ENTER TO RIGHT BRANCH')
    root.right = build_tree(sorted_arr[mid_ind+1:])
    return root


sorted_arr = [11, 20, 29, 32, 41, 50, 65, 72, 91, 99]
minimal_tree = build_tree(sorted_arr)
