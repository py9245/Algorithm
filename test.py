import time

import sys

import heapq

sys.stdin = open('input.txt', 'r')

T = int(input())

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]
    hq = []
    heapq.heappush(hq, [0, 0, 0])
    distance[0][0] = 0

    while hq:
        move_cnt, x, y = heapq.heappop(hq)
        # print(f"x : {x}, y : {y}, 현재 이동거리 : {move_cnt}")
        if distance[x][y] < move_cnt:
            continue

        if x == (N - 1) and y == (N - 1):
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
                continue

            nxt_move_cnt = move_cnt + 1

            if distance[nx][ny] <= nxt_move_cnt:
                continue

            heapq.heappush(hq, [nxt_move_cnt, nx, ny])
            distance[nx][ny] = nxt_move_cnt
    print(f"#{case} {-1 if distance[N - 1][N - 1] == float('inf') else distance[N - 1][N - 1]}")
