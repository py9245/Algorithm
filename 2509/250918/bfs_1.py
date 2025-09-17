import sys
from collections import deque
sys.stdin = open('input.txt', "r")

from collections import deque

T = int(input())
N = 4

for case in range(1, T + 1):
    K = int(input())
    gears = [deque(map(int, input().split())) for _ in range(N)]

    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1

        can = [gears[i][2] != gears[i+1][-2] for i in range(N-1)]

        rotate_dirs = [0] * N
        rotate_dirs[n] = d

        dir = d
        for i in range(n-1, -1, -1):
            if can[i]:
                dir = -dir
                rotate_dirs[i] = dir
            else:
                break

        dir = d
        for i in range(n, N-1):
            if can[i]:
                dir = -dir
                rotate_dirs[i+1] = dir
            else:
                break

        for i in range(N):
            if rotate_dirs[i]:
                gears[i].rotate(rotate_dirs[i])

    ans = sum((gears[i][0] << i) for i in range(N))
    print(f"#{case} {ans}")