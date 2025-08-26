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
        string = q.popleft()
        string_cnt[string] -= 1

    string_len = len(mKeyword) - 3
    q.append(mKeyword)
    string_cnt[mKeyword] += 1 # 더해주기
    maxcnt -= 1

    if not linked_string[string_len].get(mKeyword):
        linked_string[string_len][mKeyword] = set()

    for next_keyword in list(linked_string[string_len]):
        if next_keyword == mKeyword:
            continue

        if is_similar(next_keyword, mKeyword, len(mKeyword)):
            linked_string[string_len][next_keyword].add(mKeyword) #양방향 연결
            linked_string[string_len][mKeyword].add(next_keyword)


def top5Keyword(mRet):
    group = []
    for bucket in linked_string:
        visited = set()
        for key in bucket:
            if key in visited:
                continue
            popular = 0
            stack = [key]
            while stack:
                linked = stack.pop()
                if linked in visited or string_cnt[linked] < 1:
                    continue
                popular += string_cnt[key]
                for
