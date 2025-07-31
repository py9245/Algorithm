from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    products = {a * b for a, b in combinations(nums, 2)}

    valid = []
    mm = 0
    for p in products:
        if p < mm:
            continue
        s = str(p)
        if s == ''.join(sorted(s)):
            valid.append(p)
            mm = max(mm,p)
    answer = max(valid) if valid else -1

    print(f"#{t} {answer}")