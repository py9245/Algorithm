import sys

sys.stdin = open('input.txt', "r")

T = int(input())

def do_calculator(current_cum, next_num, cal):
    if cal == 0:
        return current_cum + next_num
    if cal == 1:
        return current_cum - next_num
    if cal == 2:
        return current_cum * next_num
    return int(current_cum / next_num)


for case in range(1, T + 1):
    N = int(input())
    calculators = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dp = {tuple(calculators): (nums[0], nums[0])}

    for i in range(1, N):
        next_dp = {}
        for key, (lo, hi) in dp.items():
            per, miner, multi, div = key
            for k, c in enumerate((per, miner, multi, div)):
                if c == 0:
                    continue

                nk = list(key)
                nk[k] -= 1
                nk = tuple(nk)
                for cur in (lo, hi):
                    v = do_calculator(cur, nums[i], k)
                    if nk not in next_dp:
                        next_dp[nk] = (v, v)
                    else:
                        a, b = next_dp[nk]
                        next_dp[nk] = (min(a, v), max(b, v))
        dp = next_dp

    mn, mx = dp[(0, 0, 0, 0)]
    print(f"#{case} {mx - mn}")