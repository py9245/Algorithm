import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    q = deque(map(int, input().split()))
    last = 0
    cnt = 0
    best = 1
    while q:
        num = q.popleft()
        if num > last:
            last = num
            cnt += 1
        else:
            if cnt > best:
                best = cnt
            cnt = 1
            last = num
    print(f"#{case} {max(cnt, best)}")