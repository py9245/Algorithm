#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
from collections import defaultdict, deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = 0
current_time = 0
board = dict() # 보드에서 겹치는지 확인
poten = dict() # id : 잠재력
worm = dict() # 지렁이마다 머리 꼬리 관리
direction = dict() # 방향 관리 초기는 1
lengths = dict()  # id : 현재 길이



class RESULT:
    def __init__(self):
        self.cnt = 0
        self.IDs = [0, 0, 0, 0, 0]


def init(N):
    global n, board, poten, current_time, worm, direction, lengths
    current_time = 0
    n = N
    board = dict()
    poten = dict()
    worm = dict()
    direction = dict()
    lengths = dict()


def simulation(cnt):
    if cnt == 0:
        return
    while cnt > 0 and worm:
        cnt -= 1
        out_bucket = set()
        head_bucket = defaultdict(list)
        for key in list(worm):
            if worm[key] == False:
                continue
            d = direction[key]
            h, t = worm[key]
            hy, hx = h
            ty, tx = t

            if poten[key] > 0:
                poten[key] -= 1
                nty, ntx = ty, tx
                lengths[key] += 1
            else:
                board[(ty, tx)].remove(key)
                if not board[(ty, tx)]:
                    del board[(ty, tx)]
                if hy != ty and hx != tx:
                    td = d + 3 if d == 0 else d - 1
                else:
                    td = d
                nty, ntx = ty + dxy[td][0], tx + dxy[td][1]

            if hy == ty or hx == tx:
                d = (d + 1) % 4
                direction[key] = d
            nhy, nhx = hy + dxy[d][0], hx + dxy[d][1]

            if not (0 <= nhy < n and 0 <= nhx < n):
                out_bucket.add(key)
                continue
            worm[key] = ((nhy, nhx), (nty, ntx))
            board.setdefault((nhy, nhx), []).append(key)
            head_bucket[(nhy, nhx)].append(key)

        to_die = set()
        gain = defaultdict(int)

        for (y, x), heads in head_bucket.items():
            bodies = [wid for wid in board.get((y, x), []) if wid not in heads and worm[wid] != False]


            # 머리머리 충돌
            if len(heads) >= 2 and not bodies:
                to_die.update(heads)
                continue

            # 머리 몸 충돌
            if bodies:
                body = bodies[0]  # 한 칸에는 원래 몸 하나만 존재
                for h in heads:
                    to_die.add(h)
                    gain[body] += lengths[h]

        for b, g in gain.items():
            if worm[b] != False and b not in to_die:
                poten[b] += g

        for wid in to_die|out_bucket:
            worm[wid] = False
            lengths[wid] = 0


def join(mTime, mID, mX, mY, mLength):
    global current_time
    if mTime > current_time:
        simulation(mTime - current_time)
    current_time = mTime

    worm[mID] = ((mY, mX), (mY + mLength - 1, mX))

    for i in range(mLength):
        board.setdefault((mY+i, mX), []).append(mID)

    poten[mID] = 0
    direction[mID] = 0
    lengths[mID] = mLength


def top5(mTime):
    global current_time
    if mTime > current_time:
        simulation(mTime - current_time)
    current_time = mTime

    alive = [(lengths[wid], wid) for wid in worm if worm[wid] != False]
    alive.sort(key=lambda x: (-x[0], -x[1]))

    ret = RESULT()
    ret.cnt = min(5, len(alive))
    for i in range(ret.cnt):
        ret.IDs[i] = alive[i][1]
    return ret

