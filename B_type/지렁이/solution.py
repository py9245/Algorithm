#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
from collections import defaultdict, deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = 0
current_time = 0
board = [[[] for _ in range(n)] for _ in range(n)] # 보드에서 겹치는지 확인
poten = dict() # id : 잠재력
worm = defaultdict(deque) # 지렁이마다 index 관리
direction = dict()


class RESULT:
    def __init__(self):
        self.cnt = 0
        self.IDs = [0, 0, 0, 0, 0]


def init(N):
    global n, board, poten, current_time, worm, direction
    current_time = 0
    n = N
    board = [[[] for _ in range(n)] for _ in range(n)]
    poten = dict()
    defaultdict(deque)
    direction = dict()


def simulation(cnt):
    if cnt == 0:
        return
    while cnt > 0 and worm:
        cnt -= 1
        del_list = []
        for key in list(worm):
            d = direction[key]
            hy, hx = worm[key][0]
            ty, tx = worm[key][-1]
            if poten[key] > 0:
                poten[key] -= 1
            else:
                worm[key].pop()
                board[ty][tx].remove(key)
            if hy == ty or hx == tx:
                direction[key] = (d + 1) % 4
            nhy, nhx = hy + dxy[d][0], hx + dxy[d][1]
            if not (0 <= nhy < n and 0 <= nhx < n):





def join(mTime, mID, mX, mY, mLength):
    global current_time
    if mTime > current_time:
        simulation(mTime - current_time)
    current_time = mTime

    for i in range(mLength):
        board[mY + i][mX].append(mID)
        worm[mID].append((mY + i, mX))

    poten[mID] = 0
    direction[mID] = 0


def top5(mTime):
    ret = RESULT()
    return ret

