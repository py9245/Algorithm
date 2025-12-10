import sys
from collections import deque


sys.stdin = open("input.txt", "r")


T = int(input())

for case in range(1, T + 1):
    q = deque(list(input()))
    s_list = []
    while q:
        string = q.popleft()
        if s_list:
            if string == s_list[-1]:
                s_list.pop()
            else:
                s_list.append(string)
        else :
            s_list.append(string)
    print(f"#{case} {len(s_list)}")