import time
from collections import deque
import sys

st = time.time()
sys.stdin = open('input.txt', 'r')

T = int(input())

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    apple_dict = {}
    for i in range(N):
        for j in range(N):
            num = board[i][j]
            if num:
                apple_dict[num] = (i, j)

    complate = [False] * (len(apple_dict) + 1)
    complate[0] = True
    visi = [[False] * N for _ in range(N)]
    visi[0][0] = True
    q = deque()
    q.append((0, 0, 0, 0, 1))

    while q:
        x, y, d, total, apple = q.popleft()

        if complate[apple]:
            continue

        if (x, y) == apple_dict[apple]:
            complate[apple] = True
            apple += 1
            visi = [[False] * N for _ in range(N)]

        if apple > len(apple_dict):
            print(f"#{case} {total}")
            break

        for i in range(2):
            nd = (d + i) % 4
            dx, dy = dxy[nd]
            nx, ny = x + dx, y + dy
            if (0 <= nx < N and 0 <= ny < N) and not visi[nx][ny]:
                q.append((nx, ny, nd, total + i, apple))

print(time.time() - st)

#-----------------------------------------------------------------

# import time
# from collections import deque
# import sys
#
# st = time.time()
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#
#     def per(arr, n, total):
#         global best
#
#         if n == 3:
#             o_1 = total + (arr[0] * arr[2]) + arr[0] + arr[0]
#             o_2 = total + (arr[0] * arr[2]) + arr[2] + arr[2]
#             o_3 = total + (arr[1] + arr[2] + arr[2])
#             o_4 = total + (arr[1] + arr[1] + arr[1])
#             o_5 = total + (arr[1] + arr[0] + arr[0])
#             best = max(best, o_1, o_2, o_3, o_4, o_5)
#             return
#
#         for i in range(n):
#             if i == 0:
#                 per(arr[i + 1:], n - 1, total + arr[i + 1])
#             elif i == (n - 1):
#                 per(arr[:i], n - 1, total + arr[i - 1])
#             else:
#                 per(arr[:i] + arr[i + 1:], n - 1, total + (arr[i + 1] * arr[i - 1]))
#
#     best = 0
#     per(nums, N, 0)
#     print(f"#{case} {best}")
# print(time.time() - st)
