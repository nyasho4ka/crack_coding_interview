import time
import collections


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.is_visited = False
        self.children = children if children else []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

    def remove_child_by_index(self, index):
        del self.children[index]

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self, root):
        self.root = root

    def dfs(self, node):
        if node is None:
            return
        self.visit(node)
        node.is_visited = True
        for child in node.children:
            if child.is_visited:
                continue
            self.dfs(child)

    def bfs(self, node, searched_node):
        node_queue = collections.deque()
        node.is_visited = True
        node_queue.append(node)

        while len(node_queue) != 0:
            n = node_queue.popleft()
            if self.visit(n, searched_node):
                return True
            for child in n.children:
                if not child.is_visited:
                    child.is_visited = True
                    node_queue.append(child)

    def route_between(self, node1, node2):
        search1 = self.bfs(node1, node2)
        search2 = self.bfs(node2, node1)
        return search1 or search2

    def visit(self, node, searched_node):
        if node == searched_node:
            return True


def create_graph():
    node1 = Node(1)
    node2 = Node(2)
    node5 = Node(5)
    node8 = Node(8)
    node_1 = Node(-1)
    node10 = Node(10)
    node6 = Node(6)
    node30 = Node(30)

    node1.add_child(node2)
    node1.add_child(node10)
    node1.add_child(node_1)

    node2.add_child(node5)

    node5.add_child(node8)
    node5.add_child(node6)

    node6.add_child(node_1)
    node6.add_child(node30)

    node8.add_child(node30)
    node30.add_child(node1)

    graph = Graph(node1)
    return graph, node1, node8


graph, node1, node8 = create_graph()
start = time.time()
if graph.route_between(node1, node8):
    print('ROUTE EXISTS!')
else:
    print('ROUTE DOESN\'T EXIST')
print(time.time() - start)
