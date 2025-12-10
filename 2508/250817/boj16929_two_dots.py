import sys
from collections import deque

sys.stdin = open("input.txt", "r")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

alpha_cnt = [set() for _ in range(26)]
alpha_arr = [[] for _ in range(N)]

for i in range(N):
    for j, v in enumerate(input()):
        num = ord(v) - 65
        alpha_cnt[num].add((i, j))
        alpha_arr[i].append(num)

for i in range(26):
    if len(alpha_cnt[i]) < 4:
        alpha_cnt[i] = set()

def bfs():
    visited = [[False] * M for _ in range(N)]
    for i in range(26):
        if not alpha_cnt[i]:
            continue

        for alpha in alpha_cnt[i]:
            x, y = alpha

            if visited[x][y]:
                continue

            visited[x][y] = True

            q = deque([[x, y, -1]])
            while q:
                x, y, nd = q.popleft()
                for d in range(4):
                    if d == nd:
                        continue
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if alpha_arr[nx][ny] == i:
                            if visited[nx][ny]:
                                return True
                            q.append([nx, ny, (d + 2) % 4])
                            visited[nx][ny] = True

print("Yes" if bfs() else "No")