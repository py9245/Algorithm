import sys
from solution import init, addKeyword, top5Keyword

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


sys.stdin = open('../sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run1() else 0
    print("#%d %d" % (tc, score), flush = True)
