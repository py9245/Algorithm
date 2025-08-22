from collections import defaultdict

def get_hash(mPiece): # 받은 5*5 별7개짜리 박스 해쉬 변환
    bit_hash = 0
    for r in range(5):
        for c in range(5):
            bit_hash <<= 1
            bit_hash += mPiece[r][c]
    return bit_hash


def get_min_key(mPlane):
    temp_key = get_hash(mPlane) #비트 기반 해쉬 변환
    temp_arr = [temp_key] # 90,180, 270도 돌린 애들도 넣어줘야하니 배열에 넣어줌
    for _ in range(3): #3번 돌려서 넣어줌
        mPlane = [list(mPlane) for mPlane in zip(*mPlane[::-1])]
        temp_arr.append(get_hash(mPlane)) #예내들도 바꿔줌
    return temp_arr


def init(N, mPlane):
    global hash_table_p, hash_table_s, hash_table_mk, key_arr
    nojuck_arr = [[0 for _ in range(N + 5)] for _ in range(N + 5)] # 누적합 기반
    key_arr = [[0 for _ in range(N + 5)] for _ in range(N + 5)] # 누적합 기준으로

    hash_table_p = defaultdict(lambda: float("INF"))
    hash_table_s = defaultdict(int) # 같은 모양 카운트할 갯수
    hash_table_mk = defaultdict(int) # 3번돌린것과 안돌린 것들 key의 벨류는 그중의 작은 값으로 다른 범위에 회전한 별이 있어도 작은 값으로 통일
    for i in range(0, N):
        for j in range(0, N):
            nojuck_arr[i][j] = mPlane[i][j] + nojuck_arr[i - 1][j] + nojuck_arr[i][j - 1] - nojuck_arr[i - 1][j - 1]

    for i in range(N):
        for j in range(N):
            if nojuck_arr[i + 4][j + 4] - nojuck_arr[i - 1][j + 4] - nojuck_arr[i + 4][j - 1] + nojuck_arr[i - 1][j - 1] == 7:
                temp_key_arr = get_min_key([row[j:j + 5] for row in mPlane[i:i + 5]])
                min_key = min(temp_key_arr)

def getCount(mPiece): #arr 2차원 배열
    return 0


def getPosition(mRow, mCol):
    return 0

