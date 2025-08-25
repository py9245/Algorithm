import sys
from collections import defaultdict

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []

    for _ in range(N):
        w, v = map(int, input().split())
        if w <= K:
            arr.append((w,v))

    dp = [0] * (K + 1)
    for w, v in arr:
        for dw in range(K - w, -1, -1):
            if not dp[dw]:
                continue
            nw = dw + w
            nv = dp[dw] + v
            if dp[nw] < nv:
                dp[nw] = nv

        if dp[w] < v:
            dp[w] = v

    print(f"#{case} {max(dp)}")



