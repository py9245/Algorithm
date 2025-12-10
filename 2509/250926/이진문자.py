import sys
from collections import deque
sys.stdin = open('input.txt', "r")

from collections import deque

T = int(input())
match_bit = [[0, 0], [0, 1], [1, 0], [1, 1]]
answer = []

for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    length = sum(arr)
    memo = []
    cnt = 0
    memo.append(arr)

    for i in range(length):
        n_memo = []
        for ar in memo:
            if i == 0:
                for idx in range(4):
                    if ar[idx]:
                        n_memo.append(ar[:idx] + [ar[idx] - 1] + ar[idx + 1:] + match_bit[idx])
            elif ar[-1] == 0:
                if ar[0]:
                    n_memo.append([ar[0] - 1] + ar[0 + 1:] + [match_bit[0][1]])
                    if i == length - 1:
                        break
                if ar[1]:
                    n_memo.append(ar[:1] + [ar[1] - 1] + ar[1 + 1:] + [match_bit[1][1]])
                    if i == length - 1:
                        break
            elif ar[-1] == 1:
                if ar[2]:
                    n_memo.append(ar[:2] + [ar[2] - 1] + ar[2 + 1:] + [match_bit[2][1]])
                    if i == length - 1:
                        break
                if ar[3]:
                    n_memo.append(ar[:3] + [ar[3] - 1] + ar[3 + 1:] + [match_bit[3][1]])
                    if i == length - 1:
                        break
        memo = n_memo[:]
    if memo:
        answer.append(f"#{case} {''.join(map(str, memo[0][4:]))}\n")
    else:
        answer.append(f"#{case} impossible\n")
print(''.join(answer))

# T = int(input())
#
# for case in range(1, T + 1):
#
#     def dfs():
#         stack = [start]
#         path = []
#
#         while stack:
#             v = stack[-1]
#             if graph[v]:
#                 next_v = graph[v].pop()
#                 stack.append(next_v)
#             else:
#                 path.append(stack.pop())
#
#         return path[::-1]
#
#
#     A, B, C, D = map(int, input().split())
#     str_001 = A + B
#     str_100 = A + C
#     str_110 = C + D
#     str_011 = B + D
#     diff_0 = str_001 - str_100
#     diff_1 = str_110 - str_011
#
#     if abs(diff_0) > 1 or abs(diff_1) > 1 or diff_0 + diff_1 != 0:
#         print(f"#{case} impossible")
#         continue
#
#     if diff_0 == 1:
#         start = 0
#     elif diff_1 == 1:
#         start = 1
#     else:
#         start = 0 if (A + B > 0) else 1
#
#     graph = {0: [], 1: []}
#     graph[0].extend([0] * A + [1] * B)
#     graph[1].extend([0] * C + [1] * D)
#
#     euler_path = dfs()
#
#     if len(euler_path) != A + B + C + D + 1:
#         print(f"#{case} impossible")
#     else:
#         result = ''.join(map(str, euler_path))
#         print(f"#{case} {result}")
