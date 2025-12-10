import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M, a, b = map(int, input().split())
    node_1 = [[] for _ in range(N + 1)]
    node_2 = [[] for _ in range(N + 1)]
    nums = list(map(int, input().split()))
    for _ in range(M):
        first = nums.pop()
        last = nums.pop()
        node_1[first].append(last)
        node_2[last].append(first)

    def sol():
        q = deque([a, b])
        common = {a, b}
        common_num = None

        while q:
            cur = q.popleft()
            for nxt in node_1[cur]:
                if nxt not in common:
                    common.add(nxt)
                    q.append(nxt)
                else:
                    common_num = nxt
                    break

        visited_back = set()
        dq = deque([common_num])
        visited_back.add(common_num)

        while dq:
            x = dq.popleft()
            for p in node_2[x]:
                if p not in visited_back:
                    visited_back.add(p)
                    dq.append(p)

        return common_num, len(visited_back)

    num, dist = sol()
    print(f"#{case} {num} {dist}")
