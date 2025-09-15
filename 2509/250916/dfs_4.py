import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = 10
N = 16

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
turn = {1: 2, 2: 1, 3: 4, 4: 3}
for _ in range(T):
    case = int(input())
    board = [input() for _ in range(N)]
    sp, ep = None, None
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "2":
                sp = (i, j)
                visited[i][j] = True
            elif board[i][j] == "3":
                ep = (i, j)
            elif board[i][j] == "1":
                visited[i][j] = True

    answer = 0
    q = deque()
    q.append(sp)
    while q:
        idx = q.popleft()
        if idx == ep:
            answer = 1
            break

        x, y = idx

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))

    print(f"#{case} {answer}")


