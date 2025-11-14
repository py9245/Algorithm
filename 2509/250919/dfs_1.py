import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')

    def dfs(nxt, total, cnt):
        global answer

        if cnt == N - 1:
            answer = min(answer, total + nums[nxt][0])
            return

        for i in range(1, N):
            if visi[i]:
                continue
            visi[i] = True
            dfs(i, total + nums[nxt][i], cnt + 1)
            visi[i] = False

    visi = [False] * N
    dfs(0, 0, 0)
    print(f"#{case} {answer}")