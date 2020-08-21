import unittest
import stack_min


class StackMinTestCase(unittest.TestCase):
    def test_stack_min(self):
        stacks_values = [
            [1, 2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7, 8],
            [100, -1, -2, 20, 0],
            [-1000, -10000, 1, 0, 10000]
        ]
        stacks_commands = [
            ['push', 'push', 'pop', 'pop', 'push', 'push', 'push', 'pop', 'push'],
            ['push', 'push', 'pop', 'push', 'push', 'push', 'push', 'pop'],
            ['push', 'push', 'push', 'push', 'pop', 'pop', 'push'],
            ['push', 'push', 'push', 'pop', 'pop', 'pop', 'push', 'push'],
        ]

        stacks = [self.create_stack(stacks_values[i], stacks_commands[i]) for i in range(len(stacks_values))]
        answers = [
            3,
            3,
            -1,
            0
        ]

    def create_stack(self, values, commands):
        stack = stack_min.StackMin()
        counter = 0
        for command in commands:
            if command == 'push':
                stack.push(values[counter])
                counter += 1
            else:
                stack.pop()
        return stack

    def test_empty_stack(self):
        self.assertEqual(
            stack_min.StackMin().min(),
            float('inf')
        )
