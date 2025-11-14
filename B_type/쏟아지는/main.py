import sys
import solution

CMD_INIT = 0
CMD_CNT = 1
CMD_POSITION = 2

MAX_SIZE = 1000

Map = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
Piece = [[0] * 5 for _ in range(5)]
Data = [0] * 40000



def init_map(N):
    idx = 0
    x = 0
    for _ in range(N // 25):
        for y in range(N):
            data = Data[idx]
            idx += 1
            bit = 1
            for m in range(25):
                Map[y][x + m] = 1 if (data & bit) else 0
                bit <<= 1
        x += 25

    dcnt = N % 25
    if dcnt != 0:
        for y in range(N):
            data = Data[idx]
            idx += 1
            bit = 1
            for m in range(dcnt):
                Map[y][x + m] = 1 if (data & bit) else 0
                bit <<= 1


def make_piece(data):
    bit = 1
    for i in range(5):
        for k in range(5):
            Piece[i][k] = 1 if (data & bit) else 0
            bit <<= 1


def run(stdin):
    ok = False
    Q = int(stdin.readline())
    for _ in range(Q):
        parts = stdin.readline().split()
        cmd = int(parts[0])

        if cmd == CMD_INIT:
            N = int(parts[1])
            cnt = int(parts[2])
            for k in range(cnt):
                Data[k] = int(stdin.readline())
            init_map(N)
            solution.init(N, Map)
            ok = True

        elif cmd == CMD_CNT:
            Data[0] = int(parts[1])
            ans = int(parts[2])
            make_piece(Data[0])
            ret = solution.getCount(Piece)
            if ret != ans:
                ok = False

        elif cmd == CMD_POSITION:
            row, col, ans = map(int, parts[1:])
            ret = solution.getPosition(row, col)
            if ret != ans:
                ok = False
        else:
            ok = False
    return ok


if __name__ == "__main__":
    stdin = sys.stdin = open('b_input.txt', 'r')
    T, MARK = map(int, stdin.readline().split())
    for tc in range(1, T + 1):
        score = MARK if run(stdin) else 0
        print(f"#{tc} {score}")
