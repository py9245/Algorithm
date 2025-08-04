T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = sorted(map(int, input().split()))
    ans = []
    for i in range(1,6):
        ans.append(nums[-i])
        ans.append(nums[i-1])
    ans = ' '.join(map(str,ans))
    print(f"#{case} {ans}")