import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    answer = 0

    for i in range(M - N + 1):
        total = 0
        for j in range(N):
            total += A[j] * B[i + j]
        answer = max(answer, total)

    print(f"#{tc} {answer}")