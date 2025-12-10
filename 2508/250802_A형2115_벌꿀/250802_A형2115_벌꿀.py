T = int(input())
 
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    honey = [] # (값, (r행의 c구간))
    ans = 0
     
    def non(o1, o2, M):
        r1, c1 = o1
        r2, c2 = o2
        if r1 != r2: #행이 다르면 당근 가능
            return True
        return c1+M-1 < c2 or c2+M-1 < c1 #행 같을때 범위 다른거 확인하는ㄱ
     
    for r in range(N):
        for c in range(N-M+1):
            v = g[r][c:c+M]
            best = 0
            for mask in range(1, 1<<M): # M이 5면 비트5개로 31가지 인덱스 조합으로 값을 구할 수 있음
                s, s2 = 0, 0
                for k in range(M):
                    if mask & (1<<k):
                        s  += v[k]
                        s2 += v[k]*v[k]
                if s <= C and s2 > best:
                    best = s2
            honey.append((best, (r, c)))
 
    honey.sort(key=lambda x: x[0], reverse=True)
 
 
    H = len(honey)
    for i in range(H):
        p1, v1_honey = honey[i]
        if p1*2 <= ans:
            break
             
        for j in range(i+1, H):
            p2, v2_honey = honey[j]
            if p1+p2 <= ans:
                break
            if non(v1_honey, v2_honey, M):
                ans = p1+p2
                break
 
    print(f'#{t} {ans}')