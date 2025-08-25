import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    nums = sorted(map(int, input().split()), reverse=True)
    total = sum(nums)

    if N <= 2:
        print(f"#{case} 1")
        continue

    fact = [1] * (N + 1)
    pow2 = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i
        pow2[i] = pow2[i - 1] * 2

    ALL = (1 << N) - 1

    def dfs(used, diff, remain, placed):
        if used == ALL:
            return 1
        left_cnt = N - placed
        if diff >= remain:
            return fact[left_cnt] * pow2[left_cnt]

        cnt = 0
        for i in range(N):
            if (used >> i) & 1:
                continue
            w = nums[i]
            nu = used | (1 << i)
            cnt += dfs(nu, diff + w, remain - w, placed + 1)
            if diff >= w:
                cnt += dfs(nu, diff - w, remain - w, placed + 1)
        return cnt

    answer = dfs(0, 0, total, 0)
    print(f"#{case} {answer}")