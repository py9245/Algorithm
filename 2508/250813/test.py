# import sys
# from collections import defaultdict
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# for case in range(1, T + 1):
#     N = int(input())
#     best = 0
#     start_num = 0
#     idx = []
#     board = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] > start_num:
#                 start_num = board[i][j]
#                 idx = [(i, j)]
#             elif board[i][j] == start_num:
#                 idx.append((i, j))
#     for x, y in idx:
#         cnt = 0
#         while True:
#             cnt += 1
#             num = board[x][y]
#             min_num = num
#             mx, my = -1, -1
#             for dx, dy in dxy:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     n_num = board[nx][ny]
#                     if min_num > n_num:
#                         mx, my = nx, ny
#                         min_num = n_num
#             if min_num == num:
#                 break
#             else:
#                 x, y = mx, my
#         if cnt > best:
#             best = cnt
#     print(f"#{case} {best}")
#
#
# --------------------------------------------------------------------------------------
#
#
# import sys
# from itertools import permutations as per
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# for case in range(1, T + 1):
#     N, M = map(int, input().split())
#     cnt = list(map(list, per(range(N), N)))
#     board = []
#
#     ans = []
#
#     for i in range(M):
#         a, b = map(int, input().split())
#         board.append([a - 1, b - 1])
#
#     for idx, c in enumerate(cnt):
#         num_dict = {v: i for i, v in enumerate(c)}
#         new_arr = list(range(N))
#         for a, b in board:
#             if num_dict[a] < num_dict[b]:
#                 continue
#             else:
#                 new_arr[a], new_arr[b] = b, a
#                 num_dict[a],  num_dict[b] = b, a
#         ans.append(new_arr)
#
#     answer = 0
#
#     for j in range(N):
#         for i in range(1, len(ans)):
#             if not (ans[i - 1][j] == ans[i][j]):
#                 break
#         else:
#             answer += 1
#
#     print(f"#{case} {answer}")


# --------------------------------------------------------------------------------------

#
# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N = int(input())
#     tree = list(map(int, input().split()))
#     max_num = max(tree)
#     dif_list = [max_num - num for num in tree]
#     cnt = 0
#
#     while any(dif_list):
#         cnt += 1
#         water = 2 if cnt % 2 == 0 else 1
#         for i in range(N):
#             if dif_list[i] == water:
#                 dif_list[i] = 0
#                 break
#         else:
#             for i in range(N):
#                 if dif_list[i] > 0:
#                     if (dif_list[i] % 2 == 0 and water == 2) or (dif_list[i] % 2 == 1 and water == 1):
#                         dif_list[i] -= water
#                         break
#             else:
#                 for i in range(N):
#                     if dif_list[i] > 2:
#                         dif_list[i] -= water
#                         break
#     print(f"#{case} {cnt}")


# --------------------------------------------------------------------------------------



import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(start, graph, n):
    vis = [False] * (n + 1)
    q = deque([start])
    vis[start] = True
    cnt = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not vis[nx]:
                vis[nx] = True
                q.append(nx)
                cnt += 1
    return cnt

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    rg = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        rg[b].append(a)

    ans = 0
    for i in range(1, N + 1):
        ta = bfs(i, g, N)
        shor = bfs(i, g, N)
        if ta + shor == N:
            ans += 1

    print(f"#{case} {ans}")


import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(start, bd, n):
    vis = [False] * (n + 1)
    q = deque([start])
    vis[start] = True
    cnt = 0
    while q:
        x = q.popleft()
        for nx in bd[x]:
            if not vis[nx]:
                vis[nx] = True
                q.append(nx)
                cnt += 1
    return cnt

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    M = int(input())
    g = [[] for _ in range(N + 1)]
    rg = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        rg[b].append(a)

    ans = 0
    for i in range(1, N + 1):
        ta = bfs(i, g, N)
        shor = bfs(i, rg, N)
        if ta + shor == N - 1:
            ans += 1

    print(f"#{case} {ans}")