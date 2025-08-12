def dfs(node, depth):
    visited[node] = True  # 방문 처리
    depths[node] = depth  # 깊이 저장
    for child in tree[node]:  # 방문하지 않은 자식 노드에 대해서 dfs 순회
        if not visited[child]:
            parent[child] = node  # 부모 노드 설정
            dfs(child, depth + 1)

    subtree_size[node] = 1  # 서브트리 크기 1로 초기화 (자기 자신)
    for child in tree[node]:  # 현재 노드의 모든 자식 노드에 대해
        # 자식 노드의 서브트리 크기를 더함
        # dfs를 빠져나온 상태이므로 자식 노드들의 서브트리 크기가 이미 구해져있음
        subtree_size[node] += subtree_size[child]


# 두 노드의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 두 노드의 깊이가 다르면, 더 깊은 노드를 얕은 노드의 깊이까지 끌어올림
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:  # a가 더 깊다면 a를 부모 노드로 올림
            a = parent[a]
        else:  # b가 더 깊다면 b를 부모 노드로 올림
            b = parent[b]

    # 현재 두 노드의 깊이는 같아진 상태이고,
    # 두 노드를 동시에 올리면서 같은 부모 노드를 찾음
    while a != b:
        # a, b를 부모 노드로 올림
        a = parent[a]
        b = parent[b]

    return a  # 최소 공통 조상 반환


"""
서브트리의 크기 
- 특정 노드를 루트로 하는 부분 트리에 포함된 모든 노드의 수 
"""
T = int(input())
for tc in range(1, T + 1):
    # 정점 수, 간선 수, 두 정점 a, b 입력
    v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = [[] for _ in range(v_cnt + 1)]  # 트리 구조를 저장, 번호가 1부터 시작하므로 +1 크게 할당
    parent = [0] * (v_cnt + 1)  # 각 노드의 부모를 저장
    depths = [0] * (v_cnt + 1)  # 각 노드의 깊이를 저장
    visited = [False] * (v_cnt + 1)  # DFS 탐색을 위해 방문 여부를 저장할 리스트
    subtree_size = [0] * (v_cnt + 1)  # 각 노드의 서브트리 크기를 저장할 리스트

    # 트리 생성
    for i in range(e_cnt):
        tree[edges[2 * i]].append(edges[2 * i + 1])

    # 루트 노드(1), 깊이(0)부터 DFS 수행
    # DFS 를 수행하면서 각 노드의 부모, 깊이, 서브트리 크기를 저장
    dfs(1, 0)

    common_res = lca(a_vertex, b_vertex)  # a와 b의 최소 공통 조상 찾기

    print(f"#{tc} {common_res} {subtree_size[common_res]}")
