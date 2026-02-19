import sys
from UserSolution import UserSolution

# 로컬 테스트용: 같은 폴더의 입력 파일로 stdin 교체
sys.stdin = open("sample_input.txt", "r", encoding="utf-8")

CMD_INIT = 1
CMD_DROP = 2
CMD_EXPLORE = 3


def run() -> bool:
    query_num = int(sys.stdin.readline())
    ok = False

    for _ in range(query_num):
        parts = sys.stdin.readline().split()
        query = int(parts[0])

        if query == CMD_INIT:
            mH = int(parts[1])
            mW = int(parts[2])
            usersolution.init(mH, mW)
            ok = True

        elif query == CMD_DROP:
            mId = int(parts[1])
            mLen = int(parts[2])
            mExitA = int(parts[3])
            mExitB = int(parts[4])
            mCol = int(parts[5])
            ret = usersolution.dropBox(mId, mLen, mExitA, mExitB, mCol)
            ans = int(parts[6])
            if ans != ret:
                ok = False

        elif query == CMD_EXPLORE:
            mIdA = int(parts[1])
            mIdB = int(parts[2])
            ret = usersolution.explore(mIdA, mIdB)
            ans = int(parts[3])
            if ans != ret:
                ok = False

    return ok


def main():
    global usersolution
    T, MARK = map(int, sys.stdin.readline().split())

    out = []
    for tc in range(1, T + 1):
        usersolution = UserSolution()
        score = MARK if run() else 0
        out.append(f"#{tc} {score}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
