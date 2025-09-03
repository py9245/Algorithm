#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
import heapq

n = 0
mlimit = 0
f_num = 0
bd_range = 0
board = []
info = {}


def init(N, mLimit):
    global n,mlimit, board, info, f_num, bd_range

    n = N
    mlimit = mLimit
    f_num = mLimit // 10
    bd_range = N // f_num + 1
    # n = 10_000, mlimit = 30_000일 때 4 * 4 블럭
    board = [[{} for _ in range(bd_range)] for _ in range(bd_range)]
    info = {}


def addRadio(K, mID, mFreq, mY, mX):
    for idx in range(K):
        i, freq, y, x = mID[idx], mFreq[idx], int(mY[idx]), int(mX[idx])
        info[i] = (y, x, freq)
        trans_y, trans_x = y // f_num, x // f_num
        board[trans_y][trans_x][(y, x)] = freq, i


def getMinPower(mID, mCount):
    y, x, freq = info[mID]
    ty, tx = y // f_num, x // f_num
    hq = []

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            next_y, next_x = ty + dy, tx + dx
            if not(0 <= next_y < bd_range and 0 <= next_x < bd_range):
                continue
            for n_idx, n_info in board[ty + dy][tx + dx].items():
                n_freq, n_i = n_info
                if mID == n_i:
                    continue

                if n_freq == freq:
                    total = 0
                else:
                    total = 1000

                ny, nx = n_idx
                total += (abs(ny - y) + abs(nx - x)) * 10
                if total <= mlimit:
                    heapq.heappush(hq, total)

    ans = 0
    for _ in range(mCount):
        if not hq:
            break
        ans += heapq.heappop(hq)

    return ans


# ID 고유번호와 주파수번호 따로 가지고있음
# y = i  x = j
# 무선 연결을 위해선 거리 * 10 파워 필요
# 주파수가 다르면 1000파워 더 필요
# 연결에 필요한 파워도 제한함
# 도시 한변의 길이 최대 10000 파워 제한 1000 ~ 30000

# board = n//[mLimt//10]+1
# id = [[] for _ in range(50001)]
# id[mid] =