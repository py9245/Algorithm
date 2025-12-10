N, L = map(int,input().split())

for l in range(L, 101):
    num = (N - (l * (l - 1) // 2)) / l
    if num < 0:
        print(-1)
        break
    if num.is_integer() and num >= 0 :
        sn = int(num) 
        print(*range(sn, sn + l))
        break
else:
    print(-1)
        