from collections import deque


class MyQueue:
    def __init__(self, stack1, stack2):
        self.stack1 = stack1
        self.stack2 = stack2

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        self.__move_to_stack2()
        elem = self.stack1.pop()
        self.__move_to_stack1()
        return elem

    def top(self):
        self.__move_to_stack2()
        elem = self.stack1[-1]
        self.__move_to_stack1()
        return elem

    def __move_to_stack2(self):
        for i in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())

    def __move_to_stack1(self):
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

    def is_empty(self):
        return len(self.stack1)
