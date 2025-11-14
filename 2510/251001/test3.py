import sys

sys.stdin = open("input.txt", "r")\

from collections import deque

T = int(input())

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visi = [[False] * N for _ in range(N)]
    best = 0
    best_val = N * N
    for i in range(N):
        for j in range(N):
            if visi[i][j]:
                continue

            visi[i][j] = True

            q = deque()
            q.append((i, j))
            cnt = 1
            min_val = board[i][j]
            while q:
                x, y = q.popleft()
                val = board[x][y]
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N) or visi[nx][ny]:
                        continue

                    nxt_val = board[nx][ny]

                    if abs(nxt_val - val) == 1:
                        visi[nx][ny] = True
                        cnt += 1
                        q.append((nx, ny))
                        if nxt_val < min_val:
                            min_val = nxt_val

            if cnt > best:
                best = cnt
                best_val = min_val
            elif cnt == best and min_val < best_val:
                best_val = min_val
    print(f"#{tc} {best_val} {best}")