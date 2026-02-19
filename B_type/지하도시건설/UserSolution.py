class UserSolution:
    w, h = 0, 0
    top_point = 0
    grid = []
    dist = []
    box_info = []

    def init(self, mH: int, mW: int) -> None:
        self.w, self.h = mW, mH
        self.top_point = mH - 1
        self.grid = [[] for _ in range(self.h)]
        self.box_info = [[] for _ in range(10001)]

    def dropBox(self, mId: int, mLen: int, mExitA: int, mExitB: int, mCol: int) -> int:
        check = False
        last_can = self.top_point
        for i in range(self.top_point, self.h):
            if not self.grid[i]:
                check = True
        return 0

    def explore(self, mIdA: int, mIdB: int) -> int:
        return -1
