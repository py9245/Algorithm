from collections import deque

T = int(input())

for case in range(1, T + 1):
    K = int(input())
    gears = []
    for _ in range(4):
        gears.append(deque(map(int, input().split())))
    for _ in range(K):
        n, d = map(int, input().split())
        nd = d
        can = [gears[0][2] != gears[1][-2], gears[1][2] != gears[2][-2], gears[2][2] != gears[3][-2]]
        if n == 1:
            if can[0]:
                gears[n].rotate(-nd)
                nd = -nd
                if can[1]:
                    gears[n + 1].rotate(-nd)
                    nd = -nd
                    if can[2]:
                        gears[n + 2].rotate(-nd)

        elif n == 2:
            if can[0]:
                gears[n - 2].rotate(-nd)
            if can[1]:
                gears[n].rotate(-nd)
                nd = -nd
                if can[2]:
                    gears[n + 1].rotate(-nd)

        elif n == 3:
            if can[2]:
                gears[n].rotate(-nd)
            if can[1]:
                gears[n - 2].rotate(-nd)
                nd = -nd
                if can[0]:
                    gears[n - 3].rotate(-nd)

        else:
            if can[2]:
                gears[n - 2].rotate(-nd)
                nd = -nd
                if can[1]:
                    gears[n - 3].rotate(-nd)
                    nd = -nd
                    if can[0]:
                        gears[n - 4].rotate(-nd)
        gears[n - 1].rotate(d)
    ans = 0
    for i in range(4):
        if gears[i][0]:
            ans += (2 ** i)

    print(f"#{case} {ans}")