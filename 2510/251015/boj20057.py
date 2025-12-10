dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

lost_sand = [0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01]

lost = [
    [[0, -3], [-1, -2], [1, -2], [-1, -1], [1, -1],
     [-2, -1], [2, -1], [-1, 0], [1, 0], [0, -1]],

    [[3, 0], [2, -1], [2, 1], [1, -1], [1, 1],
     [1, -2], [1, 2], [0, -1], [0, 1], [1, 0]],

    [[0, 3], [-1, 2], [1, 2], [-1, 1], [1, 1],
     [-2, 1], [2, 1], [-1, 0], [1, 0], [0, 1]],

    [[-3, 0], [-2, -1], [-2, 1], [-1, -1], [-1, 1],
     [-1, -2], [-1, 2], [0, -1], [0, 1], [-1, 0]]
]

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

sx = sy = N // 2

turn_power = 1
cnt = 0
turn = 0
answer = 0


def sand(x, y, d):
    global answer

    current_sand = board[x + dxy[d][0]][y + dxy[d][1]]
    total = 0

    for idx, s in zip(lost[d], lost_sand):
        ls = int(s * current_sand)
        total += ls
        nx, ny = x + idx[0], y + idx[1]
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += ls
        else:
            answer += ls
    if 0 <= x + dxy[d][0] * 2 < N and 0 <= y + dxy[d][1] * 2 < N:
        board[x + dxy[d][0] * 2][y + dxy[d][1] * 2] += (current_sand - total)
    else:
        answer += (current_sand - total)


for _ in range(N ** 2 - 1):
    sand(sx, sy, turn)
    cnt += 1
    sx, sy = sx + dxy[turn][0], sy + dxy[turn][1]
    if cnt == turn_power:
        turn = (turn + 1) % 4
    elif cnt == turn_power * 2:
        cnt = 0
        turn = (turn + 1) % 4
        turn_power += 1

print(answer)