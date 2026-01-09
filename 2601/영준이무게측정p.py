import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    parent = list(range(N + 1))
    dist = [0] * (N + 1)

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]

        cur = x

        path = []

        while cur != root:
            path.append(cur)
            cur = parent[cur]

        for p in reversed(path):
            dist[p] += dist[parent[p]]
            parent[p] = root
        
        return root

    def union(a, b, w):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_b] = root_a
            dist[root_b] = dist[a] - dist[b] + w

    answer = [f"#{tc}"]

    for _ in range(M):
        query = input().strip().split()
        a, b = int(query[1]), int(query[2])
        cmd = query[0]

        if cmd == "!":
            w = int(query[3])
            union(a, b, w)
        else:
            if find(a) != find(b):
                answer.append("UNKNOWN")
            else:
                answer.append(dist[b] - dist[a])
    print(*answer)
        