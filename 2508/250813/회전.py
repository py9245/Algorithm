import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f"#{case} {nums[M % N]}")