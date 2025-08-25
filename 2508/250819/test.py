import sys
from itertools import permutations

sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    cnt = 0
    for i in range(1 << N):
        big_num = total
        small_num = 0
        for j in range(N):
            if i & 1 << j:
                big_num -= nums[j]
                small_num += nums[j]
