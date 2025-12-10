import heapq

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    outer = []
    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            v = board[i][j]
            if v == 1:
                people.append((i, j))
            elif v > 1:
                outer.append([i, j])
                stairs.append(v)
    P = len(people)
    dists = []
    
    for x, y in people:
        dists.append([1 + abs(x - outer[0][0]) + abs(y - outer[0][1]),1 + abs(x - outer[1][0]) + abs(y - outer[1][1])])
    
    def sol(arriv, stair):
        if not arriv:
            return 0
        arriv.sort()
        heap = []
        for arr in arriv:
            if len(heap) < 3:
                heapq.heappush(heap, arr + stair)
            else:
                earliest = heapq.heappop(heap)
                start = max(arr, earliest)
                heapq.heappush(heap, start + stair)
        return max(heap)


    best = float('inf')
    
    for mask in range(2 ** P):
        arr0, arr1 = [], []
        for i in range(P):
            if mask & (1 << i):
                arr1.append(dists[i][1])
            else:
                arr0.append(dists[i][0])
        t0 = sol(arr0, stairs[0])
        t1 = sol(arr1, stairs[1])
        best = min(best, max(t0, t1))

    print(f"#{case} {best}")