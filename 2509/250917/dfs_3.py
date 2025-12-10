# import sys
# import heapq
#
# sys.stdin = open('input.txt', "r")
#
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input())) for _ in range(N)]
#     memo = [[float('inf')] * N for _ in range(N)]
#
#     hq = []
#     memo[0][0] = 0
#     heapq.heappush(hq, (0, 0, 0)) # 거리, x, y
#
#     while hq:
#         t, x, y = heapq.heappop(hq)
#
#         if x == N - 1 and y == N - 1:
#             print(f"#{case} {t}")
#             break
#
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             if not(0 <= nx < N and 0 <= ny < N):
#                 continue
#
#             nt = t + board[nx][ny]
#
#             if memo[nx][ny] <= nt:
#                 continue
#
#             heapq.heappush(hq, (nt, nx, ny))
#             memo[nx][ny] = nt


import sys
import heapq

sys.stdin = open('input.txt', "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    memo = [[float('inf')] * N for _ in range(N)]

    hq = [(0, 0, 0)]
    memo[0][0] = 0

    while hq:
        t, x, y = heapq.heappop(hq)

        if t > memo[x][y]:
            continue

        if x == N - 1 and y == N - 1:
            print(f"#{case} {t}")
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nt = t + board[nx][ny]
                if nt < memo[nx][ny]:
                    memo[nx][ny] = nt
                    heapq.heappush(hq, (nt, nx, ny))
