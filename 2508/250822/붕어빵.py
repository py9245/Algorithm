import sys
from collections import defaultdict

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M, K = map(int, input().split())
    last = 0 # 이 전 초
    minute = 0 # 이 전 손님이 왔을때 붕어빵을 못 만들고 남은 초
    remain = 0 # 남은 붕어빵
    customer = sorted(map(int, input().split()))
    for c in customer:
        # 지금 손님이 온 시간 - 전 손님 온 시간 + 이 전에 못만들고 남은 시간의 몫과 나머지
        re, mi = divmod(c - last + minute, M)
        # last 업데이트
        last = c
        # 남은 시간 업데이트
        minute = mi
        # 남은 붕어빵 + 지금 만든 붕어빵 - 1(붕어빰 주는거
        remain += re * K - 1
        if remain < 0: # 못 주면 멈춤
            print(f"#{case} Impossible")
            break
    else:
        print(f"#{case} Possible")
