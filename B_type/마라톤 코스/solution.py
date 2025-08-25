#####solution.py

def init(N):
    global n, node, tree, tree_check, tree_cnt
    n = N
    node = [[] for _ in range(N + 1)]
    tree = {}
    tree_check = {}
    tree_cnt = 0

def addRoad(K, mID, mSpotA, mSpotB, mLen):
    tree_cnt += K
    for _ in range(K):
        node[mSpotA].append(mID)
        node[mSpotB].append(mID)
        tree[mID] = (mSpotA, mSpotB, mLen)
        tree_check[mID] = True



def removeRoad(mID):
    pass


def getLength(mSpot) -> int:
    return 0