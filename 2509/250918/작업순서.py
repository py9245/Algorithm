T = 10

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nodes = [[] for _ in range(N + 1)]
    reversed_nodes = [[] for _ in range(N + 1)]

    for i in range(M):
        p, c = nums[i * 2], nums[i * 2 + 1]
        nodes[p].append(c)
        reversed_nodes[c].append(p)
    # print(nodes)
    # print(reversed_nodes)
    stack = []
    for i in range(1, N + 1):
        if not reversed_nodes[i]:
            stack.append(i)

    visited = [False] * (N + 1)
    answer = []


    while stack:
        # print(stack)
        node = stack.pop()  # 스텍의 마지막 pop
        if visited[node] or reversed_nodes[node]:  # 자식들 중의 하나 - 너는 방문한적 있니?
            continue
        visited[node] = True
        answer.append(node)
        # print(stack)
        for nn in nodes[node]:  # 그러면 니 자식들도 보자
            reversed_nodes[nn].remove(node)
            stack.append(nn)
            # 방문한적 없어? 그러면 너도 자식들이 있는지 확인해야하니 스텍에 추가해줄게

    string_answer = ' '.join(map(str,answer))
    print(f"#{case} {string_answer}")