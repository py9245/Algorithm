import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, a, b = map(int, input().split())
    dp = [[1]]
    for i in range(n):
        dp.append([1] + [dp[i][j] + dp[i][j + 1] for j in range(i)] + [1])
    print(f"#{tc} {dp[n][a]}")