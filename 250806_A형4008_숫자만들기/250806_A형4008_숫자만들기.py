T = int(input())
 
def oper(a, b, k):
    if k == 0:
        return a + b
    if k == 1:
        return a - b
    if k == 2:
        return a * b
    return int(a / b)
 
for case in range(1, T + 1):
    n = int(input())
    cnt = list(map(int, input().split()))
    num = list(map(int, input().split()))
    dp = {tuple(cnt): (num[0], num[0])}
 
    for i in range(1, n):
        next_dp = {}
        for key, (lo, hi) in dp.items():
            p, m, x, d = key
            for k, c in enumerate((p, m, x, d)):
                if c == 0: 
                    continue
                     
                nk = list(key)
                nk[k] -= 1
                nk = tuple(nk)
                for cur in (lo, hi):
                    v = oper(cur, num[i], k)
                    if nk not in next_dp:
                        next_dp[nk] = (v, v)
                    else:
                        a, b = next_dp[nk]
                        next_dp[nk] = (min(a, v), max(b, v))
        dp = next_dp
 
    mn, mx = dp[(0, 0, 0, 0)]
    print(f"#{case} {mx - mn}")