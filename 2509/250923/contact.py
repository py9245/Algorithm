import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

T = 10

for case in range(1, T + 1):
    N, M = map(int, input().split())
    tree = defaultdict(list)
    nums = list(map(int, input().split()))
    for i in range(N//2):
        p, c = nums[i * 2], nums[i * 2 + 1]
        tree[p].append(c)
    visi = set()
    tic = {M}

    while tic:
        new_tic = set()
        for n_tic in tic:
            if n_tic in visi or n_tic in new_tic:
                continue
            visi.add(n_tic)

            for n in tree[n_tic]:
                if n in visi or n in tic:
                    continue
                new_tic.add(n)
        if not new_tic:
            print(f"#{case} {max(tic)}")
            break
        tic = new_tic.copy()
