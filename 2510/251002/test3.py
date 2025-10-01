import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] * 2 + dp[i - 1]
    print(f"{tc} {dp[n]}")
