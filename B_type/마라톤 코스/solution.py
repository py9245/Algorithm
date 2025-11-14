n = 0
node = []
tree = {}
tree_check = {}
ans = -1

def init(N):
    global n, node, tree, tree_check
    n = N
    node = [[] for _ in range(N + 1)]
    tree = {}
    tree_check = {}

def addRoad(K, mID, mSpotA, mSpotB, mLen):
    for i in range(K):
        a, b, mid, dist = mSpotA[i], mSpotB[i], mID[i], mLen[i]
        node[a].append(mid)
        node[b].append(mid)
        tree[mid] = (a, b, dist)
        tree_check[mid] = True

def removeRoad(mID):
    if mID in tree_check:
        tree_check[mID] = False

def half_dfs(s, c, depth, dist, used_edges, out_list):
    if dist > 26195:
        return
    if depth == 4:
        out_list.append((c, dist, tuple(sorted(used_edges))))
        return

    for mid in node[c]:
        if not tree_check.get(mid, False):
            continue
        if mid in used_edges:
            continue
        a, b, d = tree[mid]
        nxt = b if a == c else a
        if nxt == s:
            continue

        nd = dist + d
        if nd > 26195:
            continue

        used_edges.add(mid)
        half_dfs(s, nxt, depth + 1, nd, used_edges, out_list)
        used_edges.remove(mid)

def getLength(mSpot):
    if sum(1 for v in tree_check.values() if v) < 8:
        return -1

    halves = []
    half_dfs(mSpot, mSpot, 0, 0, set(), halves)
    if not halves:
        return -1

    by_mid = {}
    for mid_node, d, used in halves:
        if d <= 26195:
            if mid_node not in by_mid:
                by_mid[mid_node] = []
            by_mid[mid_node].append((d, used))

    best = -1

    for mid_node, lst in by_mid.items():
        m = len(lst)
        if m < 2:
            continue

        lst.sort(key=lambda x: x[0], reverse=True)

        for i in range(m):
            di, ei = lst[i]
            if ((di + (lst[i+1][0] if i + 1 < m else -1)) <= best):
                break
            for j in range(i + 1, m):
                dj, ej = lst[j]
                total = di + dj
                if total <= best:
                    break

                if total > 42195:
                    continue

                if not (set(ei) & set(ej)):
                    best = total

    return best
