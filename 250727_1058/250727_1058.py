N = int(input())

fl = [[0] * N for _ in range(N)]
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j, s in enumerate(input()):
        if s == "Y" and i != j:
            fl[i][j] = 1
            fl[j][i] = 1
for i, f in enumerate(fl):
    for ii, ff in enumerate(f):
        if ff:
            ans[i][ii] = 1
            for iii, fff in enumerate(fl[ii]):
                if fff and iii != i:
                    ans[i][iii] = 1
                    
print(sum(i for i in max(ans, key=sum) if i))