from collections import deque
import sys
sys.stdin = open("input.txt", "r")


dxy = [(0,1),(0,-1),(1,0),(-1,0)]

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    price = [int(input()) for _ in range(N)]
    wight = [int(input()) for _ in range(M)]

    visited = [False] * N
    who_which_used = [0] * M
    wait = deque()
    answer = 0

    for i in range(M * 2):
        car = int(input())
        if car > 0:
            for idx in range(N):
                if not visited[idx]:
                    visited[idx] = True
                    answer += price[idx] * wight[car - 1]
                    who_which_used[-car] = idx
                    break
            else:
                wait.append(car)
        else:
            num = who_which_used[car]
            visited[num] = False
            if wait:
                wait_car = wait.popleft()
                visited[num] = True
                answer += price[num] * wight[wait_car - 1]
                who_which_used[-wait_car] = num
    print(f"#{case} {answer}")

