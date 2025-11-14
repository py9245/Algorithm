import sys, time
sys.stdin = open("251021_boj12094.txt", "r")

MAX_CNT = 10
TURN = 4
st = time.time()
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def gravity(arr):
    result = [n for n in arr if n != 0]
    merged = []
    i = 0
    max_val = 0
    while i < len(result):
        if i + 1 < len(result) and result[i] == result[i + 1]:
            new_val = result[i] * 2
            merged.append(new_val)
            max_val = max(max_val, new_val)
            i += 2
        else:
            merged.append(result[i])
            max_val = max(max_val, result[i])
            i += 1
    return merged + [0] * (N - len(merged)), max_val

def canonical_key(board):
    b = board
    rots = []
    for _ in range(4):
        rots.append(tuple(tuple(row) for row in b))
        b = [list(reversed(col)) for col in zip(*b)]
    return min(rots)

def count_zeros(b):
    return sum(x == 0 for row in b for x in row)

def dfs(cnt, arr, max_num, stg=0):
    global answer, bp, best_depth

    key = canonical_key(arr)
    if key in best_depth and best_depth[key] <= cnt:
        return
    best_depth[key] = cnt

    if max_num * (1 << (MAX_CNT - cnt)) <= answer:
        return

    answer = max(answer, max_num)
    if answer == best_score:
        bp = True
        return

    if cnt == MAX_CNT:
        return

    base_zero = count_zeros(arr)

    for _ in range(TURN):
        n_arr = []
        m_num = 0

        for c in range(N):
            col = [arr[c][r] for r in range(N)]
            merged_col, col_max = gravity(col)
            m_num = max(m_num, col_max)
            n_arr.append(merged_col)

        new_board = [list(row) for row in zip(*n_arr)]

        if new_board != arr:
            nz = count_zeros(new_board)
            next_stg = stg + 1 if (m_num <= max_num and nz <= base_zero) else 0
            if next_stg <= 2:
                dfs(cnt + 1, new_board, max(max_num, m_num), next_stg)

        arr = [list(reversed(col)) for col in zip(*arr)]

answer = 0
best_num = sum(j for i in board for j in i)
best_score = 1 << (best_num.bit_length() - 1)
bp = False
best_depth = {}

dfs(0, board, max(map(max, board)))
print(answer)

print(time.time() - st)