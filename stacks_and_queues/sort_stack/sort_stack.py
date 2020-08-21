from collections import deque
import random

def sort_stack(stack1, stack2):
    if len(stack1) <= 1:
        return stack1

    counter = 0
    while counter < len(stack1):
        put_max_on_bottom(stack1, stack2, counter)
        counter += 1
    return stack1


def put_max_on_bottom(stack1, stack2, counter):
    max_value = float('-inf')
    # put max value on bottom
    for i in range(len(stack1) - counter):
        if stack1[-1] > max_value:
            if max_value != float('-inf'):
                stack2.append(max_value)
            max_value = stack1.pop()
        else:
            stack2.append(stack1.pop())
    stack1.append(max_value)
    for i in range(len(stack2)):
        stack1.append(stack2.pop())


stack1 = deque([random.randint(0, 1000) for _ in range(1000)])
stack2 = deque([])
print(sort_stack(stack1, stack2))
