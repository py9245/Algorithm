from collections import deque

for t in range(1, 11):
    dump = int(input())
    nums = deque(sorted(map(int, input().split())))

    cnt = dump
    while cnt and nums[-1] - nums[0] > 1:
        hi = nums.pop()
        lo = nums.popleft()  # 최솟값

        hi -= 1
        lo += 1
        cnt -= 1
        nums.append(hi)
        nums.append(lo)
        nums = deque(sorted(nums))

    print(f"#{t} {nums[-1] - nums[0]}")