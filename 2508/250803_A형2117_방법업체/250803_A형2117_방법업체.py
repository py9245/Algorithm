from collections import defaultdict
 
T = int(input())
 
for case in range(1, T + 1):
    N, M = map(int, input().split())
    home = [(i,j) for i in range(N) for j, v in enumerate(map(int, input().split())) if v]
 
    best = 0
    for K in range(1, N+2): # N + 1까지 포함하여 검사함
        cost = K*K + (K-1)*(K-1)
     
        cnt = defaultdict(int) 
     
        for (i, j) in home:
            for dx in range(-(K-1), K):
                x = i + dx
                if not (0 <= x < N):
                    continue
                rem = (K-1) - abs(dx)
                y1, y2 = j - rem, j + rem
                for y in range(max(0, y1), min(N, y2+1)):
                    cnt[(x, y)] += 1
     
 
        for (x, y), c in cnt.items():
            profit = c * M - cost
            if profit >= 0:
                best = max(best, c)
    print(f"#{case} {best}")