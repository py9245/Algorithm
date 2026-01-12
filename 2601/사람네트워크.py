import sys

sys.stdin = open("input2.txt", "r")

from collections import deque

INF = 10 ** 9

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    node = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            used = arr[i * N + j + 1]
            if used : node[i].append(j)
    
    answer = INF

    for n in range(N):

        dist = [INF] * N
        queue = deque()
        queue.append([n, 0])
        dist[n] = 0
        current_min_total = 0
        while queue:
            if current_min_total >= answer:
                break
            c_node, cnt = queue.popleft()
            n_cnt = cnt + 1
            for n_node in node[c_node]:
                if current_min_total >= answer:
                    break

                if dist[n_node] <= n_cnt:
                    continue
                
                current_min_total += n_cnt
                dist[n_node] = n_cnt
                queue.append([n_node, n_cnt])
        
        answer = min(answer, sum(i for i in dist if i != INF))

    print(f"#{tc} {answer}")