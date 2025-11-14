import sys
from solution import init, build, demolish

CMD_INIT = 1
CMD_BUILD = 2
CMD_DEMOLISH = 3


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
        elif cmd == CMD_BUILD:
            mLength = int(next(input_iter))
            ret = build(mLength)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_DEMOLISH:
            mAddr = int(next(input_iter))
            ret = demolish(mAddr)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run1() else 0
        print("#%d %d" % (tc, score), flush=True)
