import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    student = [i - 1 for i in map(int, input().split())]
    visited = -1
    answer = 0

    for i in range(N):
        if student[i] >= 0:
            cnt = 0
            end_point = {i: cnt}
            idx = i

            while True:
                n_idx = student[idx]
                student[idx] = -1
                cnt += 1
                if n_idx in end_point:
                    answer += end_point[n_idx]
                    break
                if student[n_idx] < 0:
                    answer += cnt
                    break
                end_point[n_idx] = cnt
                idx = n_idx

    print(answer)