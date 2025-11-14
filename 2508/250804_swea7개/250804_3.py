T = int(input())
 
for case in range(1, T + 1):
    N, M = map(int,input().split())
    tr = [0] * N
    for i in range(1, M + 1):
        L, R = map(int,input().split())
        L = L - 1
        for idx in range(L, R):
            tr[idx] = i
    print(f"#{case} {' '.join(map(str,tr))}")