import collections


class StackMin:
    def __init__(self):
        self.stack = collections.deque()
        self.min_stack = collections.deque([float('inf')])

    def push(self, value):
        self.stack.append(value)
        if value < self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

    def is_empty(self):
        return bool(self.stack)

    def __str__(self):
        return 'Stack: {}\nMin stack :{}'.format(self.stack, self.min_stack)

    def __repr__(self):
        return self.__str__()
