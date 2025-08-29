#####solution.py
import heapq

n = 0
k = 0
tree = []
ans = -1


def init(N, K, sCity, eCity, mLimit):
    global n, k, tree
    n = N
    k = K
    tree = [[] for _ in range(n)]

    for i in range(k):
        s, e, l = sCity[i], eCity[i], mLimit[i]
        tree[s].append((e, l))
        tree[e].append((s, l))


def add(sCity, eCity, mLimit):
    tree[sCity].append((eCity, mLimit))
    tree[eCity].append((sCity, mLimit))



def calculate(sCity, eCity, M, mStopover):
    finished = set()
    finished.add(sCity)
    m_stop = set(mStopover)
    m_stop.add(sCity)
    m_stop.add(eCity)

    recode = [0] * n
    recode[sCity] = 300000
    hq = []

    for node, limit in tree[sCity]:
        heapq.heappush(hq, (-limit, node))
        recode[node] = limit

    while hq and len(m_stop - finished) > 0:
        limit, nd = heapq.heappop(hq)
        limit = -limit
        if recode[nd] > limit:
            continue

        for n_node, n_limit in tree[nd]:
            min_limit = min(recode[nd], n_limit)
            if recode[n_node] < min_limit:
                if n_node in finished:
                    finished.remove(n_node)
                recode[n_node] = min_limit
                heapq.heappush(hq, (-min_limit, n_node))

        finished.add(nd)

    if len(m_stop - finished) > 0:
        return -1

    best = 30001
    for st in m_stop:
        best = min(best, recode[st])

    return best
