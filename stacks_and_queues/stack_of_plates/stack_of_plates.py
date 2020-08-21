from collections import deque


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.current_stack = 0
        self.__add_stack()

    def __init_stacks(self):
        self.__add_stack()

    def push(self, value):
        if len(self.stacks[self.current_stack]) == self.capacity:
            self.__add_stack()
        self.stacks[self.current_stack].append(value)

    def __add_stack(self):
        self.stacks.append(deque())
        self.current_stack = len(self.stacks) - 1

    def pop(self):
        if len(self.stacks[self.current_stack]) == 0 and \
                self.current_stack != 0:
            self.__remove_stack()
        if self.current_stack == 0 and \
                len(self.stacks[self.current_stack]) == 0:
            raise Exception('STACK IS EMPTY!')
        return self.stacks[self.current_stack].pop()

    def __remove_stack(self, index=None):
        if index is not None:
            del self.stacks[index]
        else:
            self.stacks.pop()
        self.current_stack = len(self.stacks) - 1

    def popAt(self, index):
        elem = self.stacks[index].pop()
        if len(self.stacks[index]) == 0 and len(self.stacks) > 1:
            self.__remove_stack(index)
        return elem
