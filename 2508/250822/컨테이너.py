import sys
from collections import defaultdict

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    container = sorted(map(int,input().split()), reverse=True)
    truck = sorted(map(int,input().split()), reverse=True)

    last = 0
    answer = 0
    lc = len(container)
    for t in range(min(M, N)):
        for c in range(last,lc):
            last += 1
            if truck[t] >= container[c]:
                answer += container[c]
                break
    print(f"#{case} {answer}")