import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = deque(enumerate(map(int, input().split()), 1))
    q = deque()
    last = 0
    cnt = N
    while nums or q:
        if cnt == 0 or not nums:
            i, p = q.popleft()
            if p > 0:
                q.append((i, p // 2))
            else:
                last = i
                cnt += 1
        if cnt > 0 and nums:
            i, p = nums.popleft()
            q.append((i, p // 2))
            cnt -= 1

    print(f"#{case} {last}")