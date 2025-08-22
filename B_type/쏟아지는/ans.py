from collections import defaultdict
import heapq


def get_hash(mPiece : list[list[int]]) -> int:
    bit_hash = 0
    for r in range(5):
        for c in range(5):
            bit_hash <<= 1
            bit_hash += mPiece[r][c]
    return bit_hash


def get_min_key(mPlane: list[list[int]]):
    temp_key = get_hash(mPlane)
    temp_arr = [temp_key]
    for _ in range(3):
        mPlane = [list(mPlane) for mPlane in zip(*mPlane[::-1])]
        temp_arr.append(get_hash(mPlane))
    return temp_arr


def init(N: int, mPlane: list[list[int]]) -> None:
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


def getCount(mPiece: list[list[int]]) -> int:
    temp_key = hash_table_mk[get_hash(mPiece)]
    return hash_table_s[temp_key]


def getPosition(mRow: int, mCol: int) -> int:
    temp_key = key_arr[mRow][mCol]
    return hash_table_p[temp_key]