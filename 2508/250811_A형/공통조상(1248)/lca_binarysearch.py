from math import log2

def dfs(node, depth):
    visited[node] = True
    depths[node] = depth
    for child in tree[node]:
        if not visited[child]:
            parent[child][0] = node  # 직접적인 부모만 저장
            dfs(child, depth + 1)
    subtree_size[node] = 1
    for child in tree[node]:
        subtree_size[node] += subtree_size[child]

# 각 노드의 2의 i 승 번째 조상을 미리 계산하는 부분
# lca 를 찾기 위해 한 번에 건너뛰기 위한 전처리 과정
# 실제로 lca 를 찾을 때, 비트연산자를 이용해서 2의 배수로 건너뛰기 때문에
# 지수값에 활용될 i 를 저장
def update_ancestor():
    for i in range(1, max_depth):
        for node in range(1, v_cnt + 1):
            if parent[node][i-1] != -1:
                parent[node][i] = parent[parent[node][i-1]][i-1]

def lca(a, b):
    if depths[a] < depths[b]:
        a, b = b, a

    # 깊이 맞추기
    for i in range(max_depth - 1, -1, -1):
        """
        여기가 제일 하이라이트  
        """
        # 비트연산자로 2의 배수만큼 한 번에 이동
        if depths[a] - depths[b] >= (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    # 공통 조상 찾기
    for i in range(max_depth - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

T = int(input())
for tc in range(1, T + 1):
    v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())
    edges = list(map(int, input().split()))

    max_depth = int(log2(v_cnt)) + 1
    tree = [[] for _ in range(v_cnt + 1)]
    parent = [[-1] * max_depth for _ in range(v_cnt + 1)]
    depths = [0] * (v_cnt + 1)
    visited = [False] * (v_cnt + 1)
    subtree_size = [0] * (v_cnt + 1)

    for i in range(e_cnt):
        tree[edges[2 * i]].append(edges[2 * i + 1])

    dfs(1, 0)
    update_ancestor()

    common_ancestor = lca(a_vertex, b_vertex)

    print(f"#{tc} {common_ancestor} {subtree_size[common_ancestor]}")