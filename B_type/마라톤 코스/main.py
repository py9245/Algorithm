#####main.py
import sys
from solution import init, addRoad, removeRoad, getLength

CMD_INIT = 100
CMD_ADD = 200
CMD_REMOVE = 300
CMD_GETLEN = 400

rid = [0 for _ in range(10)]
sa = [0 for _ in range(10)]
sb = [0 for _ in range(10)]
length = [0 for _ in range(10)]

def run1():
    global rid, sa, sb, length
    Q = int(input())
    okay = False
    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            n = int(next(input_iter))
            init(n)
            okay = True
        elif cmd == CMD_ADD:
            strTmp = next(input_iter)
            k = int(next(input_iter))
            for i in range(k):
                in_iter = iter(input().split())
                strTmp = next(in_iter)
                rid[i] = int(next(in_iter))
                strTmp = next(in_iter)
                sa[i] = int(next(in_iter))
                strTmp = next(in_iter)
                sb[i] = int(next(in_iter))
                strTmp = next(in_iter)
                length[i] = int(next(in_iter))
            addRoad(k, rid, sa, sb, length)
        elif cmd == CMD_REMOVE:
            strTmp = next(input_iter)
            mid = int(next(input_iter))
            removeRoad(mid)
        elif cmd == CMD_GETLEN:
            strTmp = next(input_iter)
            mid = int(next(input_iter))
            ret = getLength(mid)
            strTmp = next(input_iter)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run1() else 0
    print("#%d %d" % (tc, score), flush = True)