import time
import collections


class Link:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head if head else Link(None, None)
        self.__close_list()

    def __close_list(self):
        if self.head.next is None:
            self.head.next = self.head
            return

        n = self.head
        while n.next is not None:
            n = n.next
        n.next = self.head

    def append(self, value):
        if self.head.value is None:
            self.head = Link(value)
            self.__close_list()
            return

        n = self.head.next
        while n.next is not self.head:
            n = n.next

        new_link = Link(value, self.head)
        n.next = new_link

    def step(self):
        n = self.head
        yield None
        while True:
            is_stop = yield n
            if is_stop:
                return
            n = n.next

    def get_generator(self):
        cg = self.step()
        cg.send(None)
        return cg

    def __str__(self):
        result = '{}->'.format(self.head)

        n = self.head.next
        while n is not self.head:
            result += '{}->'.format(n)
            n = n.next
        return result[:-2]


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


class Dependencies:
    def __init__(self):
        self.circular_queue = None
        self.dependencies_hash = dict()

    def build_dependencies(self, projects, dependencies):
        for project in projects:
            if project not in self.dependencies_hash:
                self.dependencies_hash[project] = []
            for dependency in dependencies:
                independent, dependent = dependency
                if dependent == project:
                    self.dependencies_hash[dependent].append(independent)

    def build_circular_queue(self):
        self.circular_queue = CircularLinkedList()
        for project in self.dependencies_hash.keys():
            self.circular_queue.append(project)

    def build_order(self):
        order = []

        circular_queue = self.circular_queue.get_generator()
        is_stop = False
        while len(order) != len(self.dependencies_hash):
            project = circular_queue.send(is_stop)
            if len(self.dependencies_hash[project.value]) == 0:
                if project.value not in order:
                    order.append(project.value)
                    continue
            counter = 0
            for dependency in self.dependencies_hash[project.value]:
                if dependency in order:
                    counter += 1
            if counter == len(self.dependencies_hash[project.value]):
                if project.value not in order:
                    order.append(project.value)
        return order

    def dfs(self, node):
        if node is None:
            return
        self.visit(node)
        node.is_visited = True
        for child in node.children:
            if child.is_visited:
                continue
            self.dfs(child)

    def bfs(self, node):
        node_queue = collections.deque()
        node.is_visited = True
        node_queue.append(node)

        while len(node_queue) != 0:
            n = node_queue.popleft()
            if self.visit(n):
                return True
            for child in n.children:
                if not child.is_visited:
                    child.is_visited = True
                    node_queue.append(child)

    def visit(self, node):
        pass


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
d = Dependencies()
d.build_dependencies(projects, dependencies)
d.build_circular_queue()
order = d.build_order()
print(d.circular_queue)
print(d.dependencies_hash)
print(order)
