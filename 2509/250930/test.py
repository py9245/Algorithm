# import sys
#
# sys.stdin = open('input.txt', 'r')
# import time
#
# st = time.time()

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    # A = set(range(1, 500000))
    B = set(map(int, input().split()))
    cnt = 0
    for i in B:
        if i in A:
            cnt += 1
    # B = set(range(250000, 750000))
    print(f"#{tc} {cnt}")
# print(time.time() - st)
