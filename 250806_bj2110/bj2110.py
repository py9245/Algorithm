import sys
input = sys.stdin.readline


def can_place(dist):
    cnt, last = 1, nums[0]
    for x in new_nums:
        if x - last >= dist:
            cnt += 1
            last = x
            if cnt == C:
                return True
    return False


N, C = map(int, input().split())
nums = sorted(int(input()) for _ in range(N))
lo, hi = 1, (nums[-1] - nums[0]) // (C - 1)
ans = 0
new_nums = nums[1:]
while lo <= hi:
    mid = (lo + hi) // 2
    if can_place(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
