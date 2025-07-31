T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    nums = { 0 }
    for s in score:
        nl = set()
        for ss in nums:
            nl.add(ss + s)
        nums |= nl
    print(f"#{t} {len(nums)}")