import time


def triple_step(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


hash_for_triple_step = dict()


def triple_step_with_memo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n in hash_for_triple_step:
        return hash_for_triple_step[n]
    value = triple_step_with_memo(n-1) + triple_step_with_memo(n-2) + triple_step_with_memo(n-3)
    hash_for_triple_step[n] = value
    return value


start_time = time.time()
print(triple_step(8))
print('triple_step(8) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
print(triple_step(10))
print('triple_step(10) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
print(triple_step(20))
print('triple_step(20) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
print(triple_step(30))
print('triple_step(30) has taken {} ms'.format(time.time() - start_time))

print('MEMOIZATION APPROACH')
start_time = time.time()
print(triple_step_with_memo(8))
print('triple_step(8) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
hash_for_triple_step = dict()
print(triple_step_with_memo(10))
print('triple_step(10) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
hash_for_triple_step = dict()
print(triple_step_with_memo(20))
print('triple_step(20) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
hash_for_triple_step = dict()
print(triple_step_with_memo(30))
print('triple_step(30) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
hash_for_triple_step = dict()
print(triple_step_with_memo(40))
print('triple_step(40) has taken {} ms'.format(time.time() - start_time))
start_time = time.time()
hash_for_triple_step = dict()
print(triple_step_with_memo(60))
print('triple_step(60) has taken {} ms'.format(time.time() - start_time))
