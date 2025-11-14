import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = deque(sorted(map(int, input().split())))
    cnt = 0
    last = 0
    for p in people:
        cnt = (p - last) // M * K - 1 + cnt
        last = p // M * M
        if cnt < 0:
            print(f"#{case} Impossible")
            break
    else:
        print(f"#{case} Possible")