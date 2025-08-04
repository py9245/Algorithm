T = int(input())

for case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    idx = 1
    ans = 0
    while idx + K -1 < N:
        last_charge = 0
        for j in range(idx, idx + K):
            if j in charge:
                last_charge = j
        if last_charge:
            ans += 1
            idx = last_charge + 1
        else:
            print(f"#{case} 0")
            break
    else:
        print(f"#{case} {ans}")