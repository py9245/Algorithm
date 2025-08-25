import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    print(f"#{case}")

    cnt = 0
    answer = []
    add = []
    for _ in range(N):
        S, C = input().split()
        for i in range(int(C)):
            add.append(S)
            cnt += 1
            if cnt == 10:
                cnt = 0
                answer.append(add)
                add = []
    if add:
        answer.append(add)
    for ans in answer:
        print(''.join(ans))