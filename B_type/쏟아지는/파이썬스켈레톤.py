#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
from collections import defaultdict

def get_hash(mPiece):
    bit_hash = 0
    for r in range(5):
        for c in range(5):
            bit_hash <<= 1
            bit_hash += mPiece[r][c]
    return bit_hash


def get_min_key(mPlane):
    temp_key = get_hash(mPlane)
    temp_arr = [temp_key]
    for _ in range(3):
        mPlane = [list(mPlane) for mPlane in zip(*mPlane[::-1])]
        temp_arr.append(get_hash(mPlane))
    return temp_arr


def init(N, mPlane):
    global hash_table_p, hash_table_s, hash_table_mk, key_arr
    dp_arr = [[0 for _ in range(N + 5)] for _ in range(N + 5)]
    key_arr = [[0 for _ in range(N + 5)] for _ in range(N + 5)]

    hash_table_p = defaultdict(lambda: 999999999)
    hash_table_s = defaultdict(int)
    hash_table_mk = defaultdict(int)
    for i in range(0, N):
        for j in range(0, N):
            dp_arr[i][j] = mPlane[i][j] + dp_arr[i - 1][j] + dp_arr[i][j - 1] - dp_arr[i - 1][j - 1]

    for i in range(N):
        for j in range(N):
            if dp_arr[i + 4][j + 4] - dp_arr[i - 1][j + 4] - dp_arr[i + 4][j - 1] + dp_arr[i - 1][j - 1] == 7:
                temp_key_arr = get_min_key([row[j:j + 5] for row in mPlane[i:i + 5]])
                min_key = min(temp_key_arr)
                for r in range(5):
                    for c in range(5):
                        key_arr[i + r][j + c] = min_key
                for k in temp_key_arr:
                    hash_table_mk[k] = min_key
                hash_table_p[min_key] = min(hash_table_p[min_key], (i + 2) * 10000 + j + 2) # 중앙점 row * 10000
                hash_table_s[min_key] += 1 # 같은모양 가운트
    pass


def getCount(mPiece):
    temp_key = hash_table_mk[get_hash(mPiece)]
    return hash_table_s[temp_key]


def getPosition(mRow, mCol):
    temp_key = key_arr[mRow][mCol]
    return hash_table_p[temp_key]


#####main.py
#import sys

#from solution import init, getCount, getPosition

CMD_INIT = 0
CMD_CNT = 1
CMD_POSITION = 2

MAX_SIZE = 1000

Map = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
Piece = [[0 for _ in range(5)] for _ in range(5)]
Data = [0 for _ in range(40000)]

def init_map(N):
    global Map, Data
    idx = 0
    x = 0
    for i in range(int(N / 25)):
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(25):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2
        x = x + 25

    dcnt = N % 25
    if dcnt != 0:
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(dcnt):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2


def make_piece(data):
    global Piece
    bit = 1
    for i in range(5):
        for k in range(5):
            if data & bit != 0:
                Piece[i][k] = 1
            else:
                Piece[i][k] = 0
            bit = bit * 2

def _run():
    global Map, Data, Piece
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            cnt = int(next(input_iter))
            for i in range(0, cnt):
                input_iter = iter(input().split())
                Data[i] = int(next(input_iter))
            init_map(N)
            init(N, Map)
            okay = True
        elif cmd == CMD_CNT:
            Data[0] = int(next(input_iter))
            make_piece(Data[0])
            ans = int(next(input_iter))
            ret = getCount(Piece)
            if ret != ans:
                okay = False
        elif cmd == CMD_POSITION:
            row = int(next(input_iter))
            col = int(next(input_iter))
            ret = getPosition(row, col)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


#if __name__ == '__main__':
    #sys.stdin = open('sample_input.txt', 'r')
T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if _run() else 0
    print("#%d %d" % (tc, score), flush=True)