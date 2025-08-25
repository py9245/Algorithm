# import sys
# from collections import defaultdict
# sys.stdin = open("input.txt", "r")
#
#
# N, M = map(int, input().split())
# nums = sorted(map(int, input().split()))
# best = 0
# idx = []
# for i in range(N):
#     for j in range(M):
#         if board[i][j]:
#             idx.append((i, j))
#
#
#
# print(f"#{case} {best}")

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N = int(input())
#     cnt = [[] for i in range(N)]
#     visi = set()
#     answer = 0
#     for i in range(N):
#         link = list(map(int, input().split()))
#         if link[0] == 0:
#             visi.add(i)
#         else:
#             for li in link[1:]:
#                 cnt[i].append(li - 1)
#
#     if not visi:
#         print(f"#{case} -1")
#     else:
#         while answer < N * 10:
#             answer += 1
#             if len(visi) == N:
#                 print(f"#{case} {answer}")
#                 break
#             add_list = []
#             for s in range(N):
#                 if s not in visi:
#                     for c in cnt[s]:
#                         if c not in visi:
#                             break
#                     else:
#                         add_list.append(s)
#             if not add_list:
#                 print(f"#{case} -1")
#                 break
#             for k in add_list:
#                 visi.add(k)

