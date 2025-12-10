import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

import heapq

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = board[0][0]
    pq = []
    heapq.heappush(pq, [0, board[0][0], 0, 0]) # 거리합, 현재 거리, x, y

    while pq:
        total_dist, current_dist, x, y = heapq.heappop(pq)
        # print(total_dist, current_dist, x, y)
        if x == N - 1 and y == N - 1:
            break

        if total_dist > dist[x][y]:
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            ncd = board[nx][ny]
            nd = total_dist + 1 + max(0, ncd - current_dist)
            if nd >= dist[nx][ny]:
                continue
            heapq.heappush(pq, [nd, ncd, nx, ny])
            dist[nx][ny] = nd
    print(f"#{case} {dist[N - 1][N - 1]}")