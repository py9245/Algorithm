import sys
import math

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

prime = [2, 3, 5, 7, 11]

for case in range(1, T + 1):
    num = int(input())
    answer = []

    for n in prime:
        cnt = 0
        while num % n == 0:
            cnt += 1
            mod, remain = divmod(num, n)
            num = mod + remain
        answer.append(str(cnt))
    print(f"#{case} {' '.join(answer)}")