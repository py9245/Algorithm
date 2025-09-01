#####main.py
import sys
from solution import init, checkStructures, addStructures, pourIn

def input():
    return sys.stdin.readline().rstrip()


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


CMD_INIT = 1
CMD_ADD = 2
CMD_CHECK = 3
CMD_POUR = 4

MAX_N = 20
MAX_WIDTH = 500


def run1():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mWidth = int(next(input_iter))
            mHeight = int(next(input_iter))
            mIDs = [int(next(input_iter)) for i in range(N)]
            mLengths_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mLengths_tanks.append([int(next(input_iter)) for i in range(mWidth)])
            mUpShapes_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mUpShapes_tanks.append([int(next(input_iter)) for i in range(mWidth)])
            init(N, mWidth, mHeight, mIDs, mLengths_tanks, mUpShapes_tanks)
            okay = True
        elif cmd == CMD_CHECK:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = checkStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_ADD:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = addStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_POUR:
            mWater = int(next(input_iter))
            ret = pourIn(mWater)
            ans = int(next(input_iter))
            ans_height = 0
            ans_used = 0
            if ans != 0:
                ans_height = int(next(input_iter))
                ans_used = int(next(input_iter))
            if ans != 0 and ((ans != ret.ID) or (ans_height != ret.height) or (ans_used != ret.used)):
                okay = False
            elif ans == 0 and ret.ID != 0:
                okay = False
        else:
            okay = False

    return okay


if __name__ == '__main__':
    # sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run1() else 0
        print("#%d %d" % (tc, score), flush=True)
