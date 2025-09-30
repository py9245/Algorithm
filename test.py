import time
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)]
    sx, sy, ex, ey = map(int, input().split())

    visi = set()

    answer = 0

    q = deque()

    for i in range(4):
        q.append((0, sx, sy, i))

    while q:
        move_cnt, x, y, d = q.popleft()

        if (x, y, d) in visi:
            continue

        visi.add((x, y, d))

        if x == ex and y == ey:
            answer = max(answer, move_cnt)
            continue

        for idx, (dx, dy) in enumerate(dxy):
            cx, cy = x, y
            cnt = 0

            # 보드 범위 안이고 지금이 0이라면 와일문 반복
            nx, ny = cx + dx, cy + dy
            while 0 <= nx < M and 0 <= ny < N and (board[nx][ny] == 0):
                cnt += 1
                cx, cy = nx, ny
                nx, ny = cx + dx, cy + dy

            if (cx, cy, idx) in visi:
                continue

            visi.add((cx, cy, idx))
            q.append((move_cnt + cnt, cx, cy, idx))

    print(answer)
