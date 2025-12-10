import sys

sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     arr = [0 for _ in range(max(nums) + 1)]
#     for i in nums:
#         arr[i] += 1
#     answer = []
#     for i, a in enumerate(arr):
#         answer.extend([i] * a)
#     print(f"#{tc} {answer[N // 2]}")
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    AL = list(map(int, input().split()))
    BL = list(map(int, input().split()))

    AS = set(AL)
    AL.sort()
    ans = 0

    for k in BL:
        if k not in AS:
            continue

        low, high = 0, n - 1
        last = 0

        while low <= high:
            mid = (low + high) >> 1

            if AL[mid] == k:
                ans += 1
                break
            elif AL[mid] > k:
                if last == 1:
                    break
                high = mid - 1
                last = 1
            else:
                if last == -1:
                    break
                low = mid + 1
                last = -1

    print(f"#{tc} {ans}")