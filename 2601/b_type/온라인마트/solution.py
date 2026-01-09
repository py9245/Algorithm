class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

def init() -> None:
    pass

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    return -1

def closeSale(mID : int) -> int:
    return -1

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    return -1

def show(mHow : int, mCode : int) -> RESULT:
    return RESULT(-1, [0, 0, 0, 0, 0])