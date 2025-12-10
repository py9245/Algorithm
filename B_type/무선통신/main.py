#####main.py
import sys

from solution import init, addRadio, getMinPower

CMD_INIT = 0
CMD_ADDRADIO = 1
CMD_GETPOWER = 2

MAX_RADIO = 100

id1 = [0 for _ in range(MAX_RADIO)]
freq = [0 for _ in range(MAX_RADIO)]
my = [0 for _ in range(MAX_RADIO)]
mx = [0 for _ in range(MAX_RADIO)]


def run1():
    global id1, freq, my, mx
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            Limit = int(next(input_iter))
            init(N, Limit)
            okay = True
        elif cmd == CMD_ADDRADIO:
            K = int(next(input_iter))
            for i in range(0, K):
                input_iter = iter(input().split())
                id1[i] = int(next(input_iter))
                freq[i] = int(next(input_iter))
                my[i] = int(next(input_iter))
                mx[i] = int(next(input_iter))
            addRadio(K, id1, freq, my, mx)
        elif cmd == CMD_GETPOWER:
            mid = int(next(input_iter))
            cnt = int(next(input_iter))
            ret = getMinPower(mid, cnt)
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