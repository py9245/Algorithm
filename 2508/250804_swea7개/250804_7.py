for case in range(1, 11):
    N = int(input())
    high = list(map(int, input().split()))
    total = 0
    check = [-2, -1, 1, 2]
    for i in range(2, N-2):
        here = high[i]
        cloud_view = 0
        for di in check:
            ni = i + di
            if 0 <= ni < N and here > high[ni]:
                cloud_view = max(high[ni], cloud_view)
            else :
                break
        else : total += here - cloud_view
    print(f"#{case} {total}")