import sys

sys.stdin = open("input.txt", "r")

from collections import deque, defaultdict

LOG = 20

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    parents = list(map(int, input().split()))

    top_down = [[] for _ in range(N + 1)]
    bottom_up = [[] for _ in range(N + 1)]
    depth = [0] * (N + 1)
    
    for c, p in enumerate(parents, start=2):
        top_down[p].append(c)
        bottom_up[c].append(p)
        depth[c] = depth[p] + 1
    
    queue = deque()
    queue.append(1)
    
    root = []

    while queue:
        curr = queue.popleft()
        root.append(curr)
        curr_dep = depth[curr]
        for n in top_down[curr]:
            queue.append(n)

    def get_dist(u, v):
        original_u, original_v = u, v
        
        while depth[u] > depth[v]:
            u = bottom_up[u][0]
        while depth[v] > depth[u]:
            v = bottom_up[v][0]
            
        while u != v:
            u = bottom_up[u][0]
            v = bottom_up[v][0]
            
        lca = u
        
        return depth[original_u] + depth[original_v] - 2 * depth[lca]

    answer_dist = 0

    for idx in range(1, N):
        before = root[idx - 1]
        current = root[idx]
        
        answer_dist += get_dist(before, current)

    print(f"#{tc} {answer_dist}")