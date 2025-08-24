# 로컬에서 테스트 시
# solution.py와 main.py 파일을 구분해 주세요.
# main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

# 제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
from collections import deque, defaultdict


def is_similar(a, b):
    if len(a) != len(b):
        return False
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def init(N):
    global maxCnt, queue, string_counter, linked_list
    maxCnt = N
    queue = deque()
    string_counter = defaultdict(int)
    linked_list = [dict() for _ in range(8)]


def addKeyword(mKeyword):
    if len(queue) == maxCnt:
        first = queue.popleft()
        string_counter[first] -= 1
        if string_counter[first] <= 0:
            del string_counter[first]

    queue.append(mKeyword)
    string_counter[mKeyword] += 1

    idx = len(mKeyword) - 3

    bucket = linked_list[idx]
    keys_snapshot = list(bucket.keys())

    # 자기 노드 확보
    my_set = bucket.setdefault(mKeyword, set())

    # 같은 길이 기존 단어들과 한 글자 차이 양방향 연결
    for other in keys_snapshot:
        if other == mKeyword:
            continue
        if is_similar(mKeyword, other):
            bucket[other].add(mKeyword)
            my_set.add(other)


def top5Keyword(mRet):
    visited = set()
    groups = []

    alive = list(string_counter.keys())  # 현재 창에서 살아있는 키들만

    for seed in alive:
        if seed in visited:
            continue

        total = 0
        rep = None
        repCnt = -1

        dq = deque([seed])
        visited.add(seed)

        while dq:
            cur = dq.popleft()
            cnt = string_counter.get(cur, 0)
            if cnt > 0:
                total += cnt
                # 대표 갱신 cnt 우선, 같으이면 사전순
                if cnt > repCnt or (cnt == repCnt and (rep is None or cur < rep)):
                    repCnt = cnt
                    rep = cur

            idx = len(cur) - 3

            neighbors = linked_list[idx].get(cur)
            if not neighbors:
                continue

            # 현재 창에서 count>0 인 애들만 확장
            for nxt in neighbors:
                if nxt not in visited and string_counter.get(nxt, 0) > 0:
                    visited.add(nxt)
                    dq.append(nxt)

        if total > 0:
            groups.append((total, rep))

    groups.sort(key=lambda x: (-x[0], x[1]))

    retSize = min(5, len(groups))
    for i in range(retSize):
        mRet[i] = groups[i][1]
    return retSize


#####main.py
# import sys
# from solution import init, addKeyword, top5Keyword

CMD_INIT = 100
CMD_ADD = 200
CMD_TOP = 300


def run1():
    Q = int(input())
    okay = False
    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            init(N)
            okay = True
        elif cmd == CMD_ADD:
            mKeyword = next(input_iter)
            addKeyword(mKeyword)
        elif cmd == CMD_TOP:
            mRet = [None for _ in range(5)]
            user_ans = top5Keyword(mRet)
            correct_ans = int(next(input_iter))
            if user_ans != correct_ans:
                okay = False
            for i in range(correct_ans):
                correct_keyword = next(input_iter)
                if correct_keyword != mRet[i]:
                    okay = False
        else:
            okay = False
    return okay


# sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run1() else 0
    print("#%d %d" % (tc, score), flush=True)
