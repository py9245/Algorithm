import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(T):
    M, N, K = map(int, input().split())
    g = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        g[x][y] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if g[i][j]:
                ans += 1
                q = deque([(i, j)])
                g[i][j] = 0

                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N and g[nx][ny]:
                            g[nx][ny] = 0
                            q.append((nx, ny))

    print(ans)