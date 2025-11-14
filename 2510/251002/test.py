import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    items = sorted([list(map(int, input().split())) for _ in range(M)])

    dp = [0] * (N + 1)
    for w, c in items:
        new_dp = dp[:]
        for i in range(N - w + 1):
            if dp[i]:
                new_dp[i + w] = max(new_dp[i + w], dp[i] + c)
        new_dp[w] = max(new_dp[w], c)
        dp = new_dp

    print(f"#{tc} {max(dp)}")
