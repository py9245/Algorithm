T = int(input())

for case in range(1, T + 1):
    bus_stop = [0] * 5001
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            bus_stop[i] += 1
    P = int(input())
    ans = ' '.join(str(bus_stop[int(input())]) for _ in range(P))
    print(f"#{case} {ans}")