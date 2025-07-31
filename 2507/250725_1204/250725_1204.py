T = int(input())
 
for t in range(1, T + 1):
    a = input()
    cd = [0] * 101
    for i in map(int, input().split()):
        cd[i] += 1
    cd.reverse()
    print(f"#{t} {100 - cd.index(max(cd))}")