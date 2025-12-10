import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

T = int(input())

for case in range(1, T + 1):
    V, E, F, S = map(int, input().split())
    nums = list(map(int, input().split()))
    parent = [[] for _ in range(V + 1)]
    child = [0] * (V + 1)

    for i in range(E):
        a, b = nums[2 * i], nums[2 * i + 1]
        parent[a].append(b)
        child[b] = a
    visi = set()
    ans_node = 0
    q = deque()
    q.append(F)
    q.append(S)

    while q:
        node = q.popleft()
        if node in visi:
            ans_node = node
            break

        visi.add(node)

        n_node = child[node]

        if n_node == 0:
            continue
        q.append(n_node)

    ans = 1
    par = [ans_node]
    while par:
        n_p = par.pop()
        for a in parent[n_p]:
            par.append(a)
            ans += 1

    print(f"#{case} {ans_node} {ans}")


