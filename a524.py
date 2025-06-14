from itertools import permutations

try:
    while True:
        n = int(input())
        nums = list(range(1, n + 1))
        for p in permutations(nums):
            print(*p)
except EOFError:
    print("EOF")
