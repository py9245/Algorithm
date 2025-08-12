import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


for case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_num = 0
    start_idx = []
    for i in range(N): # 등산로 보드 초기화, 높은산, 높은산 인덱스 확보
        for j, v in enumerate(map(int, input().split())):
            board[i][j] = v
            if v > max_num:
                max_num = v
                start_idx = [(i,j)]
            elif v == max_num:
                start_idx.append((i, j))
    best = [0]

    def dfs(num, x, y, tr, total, vi):
        if total > best[0]:
            best[0] = total
        vi[x][y] = True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if vi[nx][ny]:
                    continue
                n_num = board[nx][ny]
                if num > n_num:
                    nvi = [col[:] for col in vi]
                    dfs(n_num, nx, ny, True, total + 1, nvi)
                else:
                    if tr and n_num - num < K:
                        nvi = [col[:] for col in vi]
                        dfs(num - 1, nx, ny, False, total + 1, nvi)


    for i, j in start_idx:
        dfs(max_num, i, j, True, 1, visited)

    print(f"#{case} {best[0]}")