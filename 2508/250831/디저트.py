import sys
sys.stdin = open('sample_input.txt', 'r')

dir_list = {
    "0": [(-1, 1), (1, 1), (-1, -1), (1, -1)],
    "1": [(1, 1), (1, -1)],
    "2": [(-1, -1), (1, -1)],
    "3": [(1, -1)],
}
next_turn = {(-1, 1): "0", (1, 1): "1", (-1, -1): "2", (1, -1): "3"}

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    best = -1
    max_cnt = (N - 1) * 2
    end_point = False

    def dfs(row, left, right, turn, cnt, visi):
        global end_point, best

        if end_point:
            return

        if left == right:
            best = max(best, cnt)
            if cnt == max_cnt:
                end_point = True
            return

        if row >= N:
            return

        for dl, dr in dir_list[turn]:
            nly, nry = left + dl, right + dr
            if not (0 <= nly < N and 0 <= nry < N):
                continue
            v1, v2 = board[row][nly], board[row][nry]
            # 디저트 번호 중복 금지
            if v1 in visi or v2 in visi:
                continue
            # 같은 행에서 서로 다른 칸인데 번호가 같으면 금지
            if v1 == v2 and nly != nry:
                continue
            visi.append(v1)
            visi.append(v2)
            dfs(row + 1, nly, nry, next_turn[(dl, dr)], cnt + 2, visi)
            visi.pop()
            visi.pop()

    for i in range(N - 2):
        for j in range(1, N - 1):
            v = [board[i][j], board[i + 1][j - 1], board[i + 1][j + 1]]
            if len(set(v)) < 3:
                continue
            dfs(i + 2, j - 1, j + 1, "0", 2, v)
    print(f"#{case} {best}")