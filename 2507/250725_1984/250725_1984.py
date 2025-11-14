T = int(input())
 
for t in range(1, T + 1):
    a = sorted(map(int, input().split()))
    mina, maxa = min(a), max(a)
    cmina, cmaxa = a.count(mina), a.count(maxa)
    avg = (sum(a) - (mina * cmina + maxa * cmaxa)) / (len(a) - cmina - cmaxa)
    print(f"#{t} {round(avg)}")