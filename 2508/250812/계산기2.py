import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = 10

for case in range(1, T + 1):
    N = int(input())
    turn = False #False는 + True *
    nums = []
    for n in input():
        if n.isnumeric():
            if turn:
                nums[-1] *= int(n)
            else:
                nums.append(int(n))
        elif n == '+':
            turn = False
        else :
            turn = True

    print(f"#{case} {sum(nums)}")
