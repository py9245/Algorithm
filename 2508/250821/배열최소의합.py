import sys
from itertools import combinations as co
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for nums in co(range(1, 13), N):
        if sum(nums) == K:
            cnt += 1
    print(f"{case} {cnt}")