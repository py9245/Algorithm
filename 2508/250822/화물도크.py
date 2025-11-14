import sys

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    dok = []
    for _ in range(N):
        dok.append(tuple(map(int, input().split())))
    dok.sort(key = lambda x: (x[1], -x[0]))

    end = dok[0][1]
    cnt = 1
    for s, e in dok[1:]:
        if e == end:
            continue
        if s >= end:
            cnt += 1
            end = e
    print(f"#{case} {cnt}")


