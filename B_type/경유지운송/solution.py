#####solution.py
from collections import defaultdict

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


def dfs(sc, ec, mstop, limi, visi):
    global ans

    if limi <= ans:
        return

    if sc == ec and not mstop:
        ans = max(ans, limi)
        return


    for node, load in tree[sc]:
        if (sc, node) in visi:
            break

        visi.append((sc, node))

        if node in mstop:
            mstop.remove(node)
            dfs(node, ec, mstop, load if limi > load else limi, visi)
            mstop.append(node)
        else:
            dfs(node, ec, mstop, load if limi > load else limi, visi)
        visi.pop()


def calculate(sCity, eCity, M, mStopover):
    global ans

    ans = -1
    dfs(sCity, eCity, mStopover, float('INF'), [sCity])
    print(ans)
    return ans
