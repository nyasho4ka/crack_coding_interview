class ThreeStacks:
    """
    Actually these structure may have
    any number of stacks in it. You just
    need to pass stack sizes in it
    """
    def __init__(self, *stack_sizes):
        self.stack_sizes = stack_sizes
        self.current_indices = self.__init_indices()
        self.start_positions = self.__init_positions()
        self.arr = self.__init_arr()

    def __init_arr(self):
        return [None] * sum(self.stack_sizes)

    def __init_indices(self):
        return [0] * len(self.stack_sizes)

    def __init_positions(self):
        positions = []
        for i in range(len(self.stack_sizes)):
            position = 0
            for j in range(i):
                position += self.stack_sizes[j]
            positions.append(position)
        return positions

    def push(self, stack_number, value):
        if stack_number > len(self.stack_sizes):
            raise Exception("There is only {} stacks!".format(len(self.stack_sizes)))

        if self.current_indices[stack_number-1] >= self.stack_sizes[stack_number-1]:
            raise Exception("Stack with {} number is full!".format(stack_number))

        stack_start_position = self.start_positions[stack_number-1]
        stack_current_index = self.current_indices[stack_number-1]

        self.arr[stack_start_position + stack_current_index] = value
        self.current_indices[stack_number-1] += 1

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            raise Exception('Stack with {} number is empty!'.format(stack_number))

        # Get previous index
        self.current_indices[stack_number-1] -= 1

        stack_start_position = self.start_positions[stack_number-1]
        stack_current_index = self.current_indices[stack_number-1]

        elem = self.arr[stack_start_position + stack_current_index]
        self.arr[stack_start_position + stack_current_index] = None

        return elem

    def top(self, stack_number):
        if self.is_empty(stack_number):
            raise Exception('Stack with {} number is empty!'.format(stack_number))

        # get previous value and don't change index
        start_stack_position = self.start_positions[stack_number-1]
        stack_current_index = self.current_indices[stack_number-1] -1

        elem = self.arr[start_stack_position + stack_current_index]
        return elem

    def is_empty(self, stack_number):
        return self.current_indices[stack_number-1] - 1 < 0

    def __str__(self):
        return self.arr

    def __eq__(self, other):
        return self.arr == other
