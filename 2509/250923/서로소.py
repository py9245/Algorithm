# import sys
# from collections import defaultdict
#
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N, M = map(int, input().split())
#     nums = {}
#     answer = ""
#     for _ in range(M):
#         cmd, a, b = map(int, input().split())
#         if cmd == 0:
#             min_node = min(a, b)
#             max_node = max(a, b)
#             if nums:
#                 change = []
#                 more_min_node = min_node
#                 if nums.get(min_node, 0) and min_node in nums:
#                     change.append(nums[min_node])
#                     more_min_node = min(nums[min_node], more_min_node)
#                 if nums.get(max_node, 0) and max_node in nums:
#                     change.append(nums[max_node])
#                     more_min_node = min(nums[max_node], more_min_node)
#                 nums[min_node] = more_min_node
#                 nums[max_node] = more_min_node
#                 while change:
#                     n = change.pop()
#                     if n == more_min_node:
#                         continue
#                     else:
#                         change.append(nums[n])
#                         nums[n] = more_min_node
#
#             else:
#                 nums[min_node] = min_node
#                 nums[max_node] = min_node
#             print(nums)
#         if cmd == 1:
#             if nums.get(a, 0) and nums.get(b, 0) and nums[a] == nums[b]:
#                 answer += "1"
#             else:
#                 answer += "0"
#
#     print(f"#{case} {answer}")


import sys

sys.stdin = open("input.txt", "r")  # 로컬 테스트 시 사용

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = {}   # parent 역할: 대표자(부모) 저장
    size = {}   # 각 집합 크기 (루트에서만 유효)

    def find(x):
        # 처음 보는 원소는 자기 자신으로 초기화 (지연 초기화)
        if x not in nums:
            nums[x] = x
            size[x] = 1
            return x
        # 루트 찾기(반복)
        root = x
        while nums[root] != root:
            root = nums[root]
        # 경로 압축
        while x != root:
            px = nums[x]
            nums[x] = root
            x = px
        return root

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        # size 큰 쪽에 작은 쪽을 붙이기
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        nums[rb] = ra
        size[ra] += size[rb]
        # rb는 더 이상 루트가 아니므로 size 항목은 선택적으로 남겨도 무방

    out = []

    for _ in range(M):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b)
        else:  # cmd == 1
            # a==b도 find로 동일 루트 처리
            out.append('1' if find(a) == find(b) else '0')

    print(f"#{case} {''.join(out)}")
