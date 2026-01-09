import sys

sys.stdin = open("input.txt", "r")

T = int(input().strip())

INF = float('inf')

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())

    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    # 자기 자신으로 가는 비용은 0
    for i in range(1, N + 1):
        dist[i][i] = 0

    # 2. 간선 정보 입력
    for _ in range(M):
        u, v, w = map(int, input().split())
        # 동일한 경로에 여러 간선이 있을 경우, 가장 작은 비용 선택
        if dist[u][v] > w:
            dist[u][v] = w

    # 3. 플로이드-워셜 알고리즘 수행 (O(N^3))
    # k: 거쳐가는 노드, i: 출발 노드, j: 도착 노드
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            # 최적화: 출발지에서 경유지까지 갈 수 없으면 스킵
            if dist[i][k] == INF:
                continue
            
            for j in range(1, N + 1):
                # (i -> k -> j) 가 (i -> j) 보다 빠르면 갱신
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 4. 출력 형식에 맞춰 결과 생성
    result = [f"#{tc}"]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] == INF:
                result.append("-1")
            else:
                result.append(dist[i][j])
    
    print(*result)