import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(1, T + 1):
    tc = int(input())
    N, cnt = map(int, input().split())
    nums = [N] * cnt
    for i in range(1, cnt):
        nums[i] *= nums[i-1]
    print(f"#{tc} {nums[-1]}")
