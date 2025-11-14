from math import gcd

def solution(n, times):
    sort_times = sorted(times)
    answer = 0
    lcm_num = sort_times[0]
    last_lcm = 0
    last_idx = 0

    def sol(n, l_num):
        total = 0
        for a in range(n):
            total,  += l_num // sort_times[a]
        return total


    for idx, num in enumerate(sort_times[1:], start = 1):
        lcm_num = num * lcm_num // gcd(lcm_num, num)
        print(idx + 1)
        if sol(idx + 1, lcm_num) >= n:
            lo, hi = last_lcm, lcm_num
            while lo <= hi:
                mid = (lo + hi) // 2
                if sol(last_idx, mid):
                    lo = mid + 1
                    answer = mid
                else:
                    hi = mid - 1
        else:
            last_lcm = lcm_num
            last_idx = idx

    return answer

print(solution(6, [7, 10]))
# 6 [7 10] -> 28
# 7 [7,10] -> 30