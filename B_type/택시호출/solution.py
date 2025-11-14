from collections import defaultdict
import heapq

n = 0
l = 0
bucket = []
texi_used = {}
bucket_mod = 0
top_5 = []
dxy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

texi_pos = {}

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

def init(N , M, L, mXs, mYs):
    global n, bucket, texi_used, bucket_mod, l, top_5, texi_pos
    l = L
    n = N
    bucket_mod = max(10, N // 10)
    bucket = [[defaultdict(list) for _ in range(10)] for _ in range(10)]
    texi_used = {}
    top_5 = []
    texi_pos = {}

    for i in range(M):
        tid = i + 1
        texi_used[tid] = [0, 0]
        x, y = mXs[i], mYs[i]
        cell = bucket[x // bucket_mod][y // bucket_mod]
        h = cell.get((x, y))
        if h is None:
            cell[(x, y)] = [tid]
        else:
            heapq.heappush(h, tid)
        texi_pos[tid] = (x, y)

def _cell_min_dist(px, py, cx, cy):
    x0 = cx * bucket_mod
    y0 = cy * bucket_mod
    x1 = min((cx + 1) * bucket_mod - 1, n - 1)
    y1 = min((cy + 1) * bucket_mod - 1, n - 1)

    if px < x0:
        dx = x0 - px
    elif px > x1:
        dx = px - x1
    else:
        dx = 0

    if py < y0:
        dy = y0 - py
    elif py > y1:
        dy = py - y1
    else:
        dy = 0

    return dx + dy

def pickup(mSX, mSY, mEX, mEY):
    sx = mSX // bucket_mod
    sy = mSY // bucket_mod

    best_dist = l + 1
    best_id = -1
    best_idx = None

    b = bucket

    for dx, dy in dxy:
        nx = sx + dx
        ny = sy + dy
        if not (0 <= nx < 10 and 0 <= ny < 10):
            continue

        cell = b[nx][ny]
        if not cell:
            continue

        # 버킷에서 나올 수 있는 최소 거리가 기존 베스트거리보다 크면 패스
        if _cell_min_dist(mSX, mSY, nx, ny) > best_dist:
            continue

        for (px, py), heap in cell.items():
            if not heap:
                continue
            d = abs(mSX - px) + abs(mSY - py)
            if d > best_dist or d > l:
                continue
            cur_id = heap[0]
            if d < best_dist or (d == best_dist and (best_id == -1 or cur_id < best_id)):
                best_dist = d
                best_id = cur_id
                best_idx = (px, py)
                if best_dist == 0:
                    break
        if best_dist == 0:
            break

    if best_id == -1:
        return -1

    ride = abs(mSX - mEX) + abs(mSY - mEY)

    ox, oy = best_idx
    ocx, ocy = ox // bucket_mod, oy // bucket_mod
    h = bucket[ocx][ocy][(ox, oy)]
    heapq.heappop(h)
    if not h:
        del bucket[ocx][ocy][(ox, oy)]

    dcx, dcy = mEX // bucket_mod, mEY // bucket_mod
    dest_cell = bucket[dcx][dcy]
    dh = dest_cell.get((mEX, mEY))
    if dh is None:
        dest_cell[(mEX, mEY)] = [best_id]
    else:
        heapq.heappush(dh, best_id)

    texi_used[best_id][0] += (best_dist + ride)
    texi_used[best_id][1] += ride

    texi_pos[best_id] = (mEX, mEY)

    return best_id

def reset(mNo):
    x, y = texi_pos[mNo]
    md, rd = texi_used[mNo]
    res = Result(x, y, md, rd)
    texi_used[mNo][0] = 0
    texi_used[mNo][1] = 0
    return res

def getBest(mNos):
    ids = texi_used.keys()
    top5 = heapq.nsmallest(5, ids, key=lambda tid: (-texi_used[tid][1], tid))
    for i in range(5):
        mNos[i] = top5[i] if i < len(top5) else 0