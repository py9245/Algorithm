from math import gcd
from collections import defaultdict, deque

n = 0
k = 0
liked_train = defaultdict(list)
train_info = {}


def link_checking(a_s, a_step, b_s, b_step, lo, hi):
    g = gcd(a_step, b_step)
    d = b_s - a_s
    if d % g:
        return False

    m1 = a_step // g
    m2 = b_step // g

    inv = 0
    if m2 != 1:
        for x in range(1, m2):
            if (m1 * x) % m2 == 1:
                inv = x
                break

    t0 = ((d // g) * inv) % m2
    L = a_step * m2
    x0 = (a_s + a_step * t0) % L

    if x0 < lo:
        x0 += ((lo - x0 + L - 1) // L) * L
    return x0 <= hi


def linking(mod_info, mid):
    a_sid, a_eid, ain = mod_info
    add_linking_train = []

    for ids, info in list(train_info.items()):
        b_sid, b_eid, bin = info

        lo, hi = max(a_sid, b_sid), min(a_eid, b_eid)
        if lo > hi:
            continue

        if link_checking(a_sid, ain, b_sid, bin, lo, hi):
            add_linking_train.append(ids)
            liked_train[ids].append(mid)

    if add_linking_train:
        liked_train[mid] = add_linking_train


def init(N, K, mId, sId, eId, mInterval):
    global n, k, liked_train, train_info

    n = N
    k = K
    liked_train = defaultdict(list)
    train_info = {}

    for i in range(K):
        mid, sid, eid, minter = mId[i], sId[i], eId[i], mInterval[i]
        linking((sid, eid, minter), mid)
        train_info[mid] = [sid, eid, minter]


def add(mId, sId, eId, mInterval):
    linking((sId, eId, mInterval), mId)
    train_info[mId] = [sId, eId, mInterval]


def remove(mId):

    del_list = liked_train.pop(mId, [])
    for key in del_list:
        lst = liked_train.get(key, [])
        if mId in lst:
            lst.remove(mId)

    train_info.pop(mId, None)


def calculate(sId, eId):

    if sId == eId:
        return 0

    start_trains = []
    goal_trains = set()
    for tid, (sid, eid, step) in train_info.items():
        if sid <= sId <= eid and (sId - sid) % step == 0:
            start_trains.append(tid)
        if sid <= eId <= eid and (eId - sid) % step == 0:
            goal_trains.add(tid)

    if not start_trains or not goal_trains:
        return -1

    for t in start_trains:
        if t in goal_trains:
            return 0

    q = deque()
    visited = set()
    for t in start_trains:
        q.append((t, 0))
        visited.add(t)

    while q:
        cur, tr = q.popleft()
        for nxt in liked_train.get(cur, []):
            if nxt in visited:
                continue
            if nxt in goal_trains:
                return tr + 1
            visited.add(nxt)
            q.append((nxt, tr + 1))

    return -1
