T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nlist = [[nums[0]]]
    for n in nums[1:]:
        nl = [] 
        for nn in nlist:
            if n > nn[-1] :
                nnn = nn + [n]
                nl.append(nnn)
        nlist.append(max(nl, key=len) if nl else [n])
    print(f"#{t} {len(max(nlist, key = len))}")