import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_common_ancestor(self, node1, node2):
        node_stack_1 = collections.deque()
        node_stack_2 = collections.deque()
        is_node_1 = self.dfs(self, node1, node_stack_1)
        is_node_2 = self.dfs(self, node2, node_stack_2)
        if not(is_node_1 and is_node_2):
            return None
        stack_diff = len(node_stack_1) - len(node_stack_2)
        if stack_diff > 0:
            for i in range(stack_diff):
                node_stack_1.popleft()
        else:
            for i in range(abs(stack_diff)):
                node_stack_2.popleft()
        for i in range(len(node_stack_1)):
            elem1 = node_stack_1.popleft()
            elem2 = node_stack_2.popleft()
            if elem1 == elem2:
                return elem1

    def dfs(self, node, searched_node, node_stack):
        # Return value: is there such element or not
        if node is None:
            return False
        if node is searched_node:
            node_stack.append(node)
            return True
        for child in node.children:
            is_node_there = self.dfs(child, searched_node, node_stack)
            if is_node_there:
                node_stack.append(node)
                return True

    def __str__(self):
        return str(self.value)


root = Node(7)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node8 = Node(8)
root.add_child(node2)
root.add_child(node8)
root.children[0].add_child(node3)
root.children[0].add_child(node4)
root.children[0].children[1].add_child(node5)

print(root.get_common_ancestor(node3, node5))
