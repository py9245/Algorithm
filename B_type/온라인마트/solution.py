#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py

class RESULT:
    def __init__(self, cnt, IDs, h, c):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5
        self.h = h
        self.c = c
        self.sol()



    def sol(self):
        min_list = []
        if self.h == 0:
            for i in range(5):
                for j in range(5):
                    cnt = 5
                    for z in range(discount_price[(i, j)]//10000, 101):
                        if cnt <= 0:
                            break
                        if not price_manager[i][j][z]:
                            continue
                        min_arr = sorted(price_manager[i][j][z].items(), key=lambda x: x[1])[:cnt]
                        cnt -= len(min_arr)
                        min_list.extend(min_arr)
        else:
            for i in range(5):
                cnt = 5
                if self.h == 1:
                    for z in range(discount_price[(self.c, i)] // 10000, 101):
                        if cnt == 0:
                            break
                        if not price_manager[self.c][i][z]:
                            continue
                        min_arr = sorted(price_manager[self.c][i][z].items(), key=lambda x: x[1])[:cnt]
                        cnt -= len(min_arr)
                        min_list.extend(min_arr)
                else:
                    for z in range(discount_price[(i, self.c)] // 10000, 101):
                        if cnt == 0:
                            break
                        if not price_manager[i][self.c][z]:
                            continue
                        min_arr = sorted(price_manager[i][self.c][z].items(), key=lambda x: x[1])[:cnt]
                        cnt -= len(min_arr)
                        min_list.extend(min_arr)

        min_list.sort(key=real_key)

        top = min_list[:5]
        self.IDs = [iid for iid, _ in top]
        self.cnt = len(self.IDs)


def real_key(item):
    iid, store_price = item
    ca, co, _ = product_dict[iid]
    return (store_price - discount_price[(ca, co)], iid)


price_manager = [[[{} for _ in range(120)] for _ in range(5)] for _ in range(5)]
product_dict = {}
discount_price = {(i, j): 0 for i in range(5) for j in range(5)}
live_count = {(i, j): 0 for i in range(5) for j in range(5)}


def init():
    global product_dict, discount_price, live_count, price_manager

    price_manager = [[[{} for _ in range(120)] for _ in range(5)] for _ in range(5)]
    product_dict = {}
    discount_price = {(i, j): 0 for i in range(5) for j in range(5)}
    live_count = {(i, j): 0 for i in range(5) for j in range(5)}


def sell(mID, mCategory, mCompany, mPrice):
    ca, co = mCategory - 1, mCompany - 1
    dis = discount_price[(ca, co)]
    store_price = mPrice + dis

    live_count[(ca, co)] += 1
    price_manager[ca][co][store_price // 10000][mID] = store_price
    product_dict[mID] = (ca, co, store_price)
    return live_count[(ca, co)]


def closeSale(mID):
    value = product_dict.get(mID, -1)
    if value == -1:
        return -1

    ca, co, store_price = value
    del product_dict[mID]
    live_count[(ca, co)] -= 1
    del price_manager[ca][co][store_price // 10000][mID]
    return store_price - discount_price[(ca, co)]


def discount(mCategory, mCompany, mAmount):
    ca, co = mCategory - 1, mCompany - 1
    discount_price[(ca, co)] += mAmount # 원래 튜플 키 할인 금액 업데이트
    dis_c = discount_price[(ca, co)] # 변수로 뽑음
    del_range = dis_c // 10000 # 버킷에 사용할 인덱스 구함 버킷 아래에 것들은 다 빈걸로 업데이트
    cnt = 0
    for i in range(del_range):
        for key_i in price_manager[ca][co][i]: # 프로덕트 딕을 없애줘야 하기 때문에 그냥 단순 순회는 진행
            del product_dict[key_i]
            cnt += 1
        price_manager[ca][co][i] = {} # 포문이 끝나면 빈 딕셔너리로 업데이트
    snap_shot = list(price_manager[ca][co][del_range].items())
    for key, value in snap_shot:
        if value <= dis_c:
            cnt += 1
            del product_dict[key]
            del price_manager[ca][co][del_range][key]
    live_count[(ca, co)] -= cnt
    return live_count[(ca, co)]

def show(mHow, mCode):
    result = RESULT(-1, [0, 0, 0, 0, 0], mHow, mCode -1)
    return result
