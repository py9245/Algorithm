import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    string = list(input())
    stack = []
    for _ in range(len(string)):
        stack.append(string.pop())

    print(''.join(stack))
