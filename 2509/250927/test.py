import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# T = int(input())
#
# for tc in range(1 ,T + 1):
#     def find(x):
#         if parents[x] != x:
#             parents[x] = find(parents[x])
#         return parents[x]
#
#     def union(x, y):
#         min_root, max_root = find(x), find(y)
#         if min_root != max_root:
#             if min_root > max_root:
#                 min_root, max_root = max_root, min_root
#             parents[max_root] = min_root
#
#
#     N, M = map(int, input().split())
#     parents = list(range(N + 1))
#     for _ in range(M):
#         a, b = map(int, input().split())
#         union(a, b)
#
#     for i in range(1, N + 1):
#         find(i)
#
#     print(f"#{tc} {len(set(parents)) - 1}")


T = int(input())

for tc in range(1 ,T + 1):
    N, M = map(int, input().split())
    parents = list(range(N + 1))
    for _ in range(M):
        a, b = map(int, input().split())
        root_a, root_b = a, b
        edit_list = []
        while parents[root_a] != root_a:
            edit_list.append(root_a)
            root_a = parents[root_a]
        while parents[root_b] != root_b:
            edit_list.append(root_b)
            root_b = parents[root_b]
        if root_a > root_b:
            root_a, root_b = root_b, root_a
        edit_list.append(root_b)
        for e in edit_list:
            parents[e] = root_a
    for i in range(1, N + 1):
        nums = []
        n = i
        while parents[n] != parents[parents[n]]:
            nums.append(n)
            n = parents[n]

        for j in nums:
            parents[j] = parents[n]


    print(f"#{tc} {len(set(parents)) - 1}")
