import sys
from collections import defaultdict

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    dp = [0] * (N//10)
    dp[0] = 1
    dp[1] = 3
    for i in range(2, N//10):
        dp[i] = dp[i - 1] + dp[i - 2] * 2
    print(f"#{case} {dp[-1]}")

