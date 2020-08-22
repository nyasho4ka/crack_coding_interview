import collections
from tree import Node, build_tree


class ListOfDepth:
    def __init__(self, tree):
        self.list = self.__init_from_tree(tree)

    def create_from_tree(self, tree):
        self.list = self.__init_from_tree(tree)

    def __init_from_tree(self, tree):
        result = []  # resulting list
        buffer_queue = collections.deque()  # buffer queue for n level

        tree_queue = collections.deque()
        tree_queue.append(tree)
        counter = 1

        n_level_queue = collections.deque()
        while len(tree_queue) > 0:
            # Get elem
            elem = tree_queue.popleft()

            # push into buffer
            if elem.left is not None:
                buffer_queue.append(elem.left)
            if elem.right is not None:
                buffer_queue.append(elem.right)

            # push into n level
            n_level_queue.append(elem)
            counter -= 1
            if counter == 0:
                result.append(n_level_queue)
                n_level_queue = collections.deque()
                # push into the tree queue
                while len(buffer_queue) > 0:
                    tree_queue.append(buffer_queue.popleft())
                    counter += 1
        return result


sorted_arr = [11, 20, 29, 32, 41, 50, 65, 72, 91, 99]
minimal_tree = build_tree(sorted_arr)
list_of_depth = ListOfDepth(minimal_tree)
for i, depth_list in enumerate(list_of_depth.list):
    print('DEPTH LEVEL: {}'.format(i))
    for elem in depth_list:
        print(elem)
