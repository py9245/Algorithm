from collections import deque, defaultdict

maxcnt = 0
linked_string = [dict() for _ in range(8)]
string_cnt = defaultdict(int)
q = deque()


def is_similar(a, b, l):
    cnt = 0

    for i in range(l):
        if a[i] != b[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True

def init(N):
    global maxcnt, linked_string, string_cnt, q

    maxcnt = N
    linked_string = [dict() for _ in range(8)]
    string_cnt = defaultdict(int)
    q = deque()

def addKeyword(mKeyword):
    global maxcnt

    if maxcnt < 1:
        string = q.pop()
        string_cnt[string] -= 1
        if string_cnt[string] <= 0:
            del string_cnt[string]

    string_len = len(mKeyword) - 3
    q.appendleft(mKeyword)
    string_cnt[mKeyword] += 1 # 더해주기
    maxcnt -= 1

    myset = linked_string[string_len].setdefault(mKeyword, set())

    for next_keyword in list(linked_string[string_len]):
        if next_keyword == mKeyword:
            continue

        if is_similar(next_keyword, mKeyword, len(mKeyword)):
            linked_string[string_len][next_keyword].add(mKeyword) #양방향 연결
            myset.add(next_keyword)


def top5Keyword(mRet):
    group = []
    visited = set()

    for s in list(string_cnt.keys()):
        if s in visited:
            continue

        ls = len(s) - 3
        popular = 0
        keyword = None
        best_cnt = -1

        queue = deque([s])
        visited.add(s)

        while queue:
            linked = queue.popleft()
            cnt = string_cnt.get(linked)
            if cnt > 0:
                popular += cnt

            if cnt > best_cnt or (cnt == best_cnt and (keyword is None or keyword > linked)):
                best_cnt = cnt
                keyword = linked

            next_bucket = linked_string[ls].get(linked)
            if not next_bucket:
                continue

            for ns in next_bucket:
                if ns not in visited and string_cnt.get(ns, 0) > 0:
                    queue.append(ns)
                    visited.add(ns)

        if popular > 0:
            group.append((popular, keyword))

    group.sort(key = lambda x: (-x[0], x[1]))

    result = min(5, len(group))
    for i in range(result):
        mRet[i] = group[i][1]

    return result
