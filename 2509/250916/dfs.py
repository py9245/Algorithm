import sys
sys.stdin = open('input.txt', "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int,input().split())
    nodes = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int,input().split())
        nodes[a].append(b)
    S, E = map(int,input().split())
    stack = [S]
    ans = set()
    ans.add(S)
    answer = 0
    while stack:
        node = stack.pop()
        if node == E:
            answer = 1
            break
        for n in nodes[node]:
            if n in ans:
                continue
            stack.append(n)
            ans.add(n)
    print(f"#{case} {answer}")


