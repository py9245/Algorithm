import heapq

n = 0
heap = []           # 빈공간: (-길이, 시작, 끝)
start_space = {}    # 시작 → 끝
end_space = {}      # 끝 → 시작
buildings = {}      # 빌딩 시작주소 → 끝주소
invalid = set()     # 힙에서 무시해야 하는 구간


def init(N):
    """토지 초기화"""
    global heap, start_space, end_space, buildings, invalid, n

    n = N
    heap = [(-N, 0, N - 1)]
    start_space = {0: N - 1}
    end_space = {N - 1: 0}
    buildings = {}
    invalid = set()




def build(mLength):
    global heap, start_space, end_space, buildings, invalid

    while heap:
        neg_len, s, e = heapq.heappop(heap)

        if (s, e) in invalid:
            invalid.remove((s, e))
            continue


        if neg_len > -mLength:
            return -1

        remain = neg_len + mLength # 음수 # -23
        right = remain // 2 # -12
        left = remain - right # -11
        left_s = s
        left_e = s - left - 1
        right_s = e + right + 1
        right_e = e
        build_id = s - left
        del start_space[s]
        del end_space[e]

        buildings[build_id] = mLength

        if left < 0:
            start_space[left_s] = left_e
            end_space[left_e] = left_s
            heapq.heappush(heap, (left, left_s, left_e))

        if right < 0:
            start_space[right_s] = right_e
            end_space[right_e] = right_s
            heapq.heappush(heap, (right, right_s, right_e))

        print(f"heap : {heap}")
        print(f"start_space : {start_space}")
        print(f"end_space : {end_space}")
        print(f"buildings : {buildings}")


        return build_id
    print(f"heap : {heap}")
    print(f"start_space : {start_space}")
    print(f"end_space : {end_space}")
    print(f"buildings : {buildings}")
    return -1



def demolish(mAddr):
    global heap, start_space, end_space, buildings, invalid
    print(f"{mAddr} {buildings}")
    if mAddr not in buildings:
        return -1

    m_length = buildings.pop(mAddr)
    left_e = mAddr - 1
    right_s = mAddr + m_length
    if left_e >= 0 and end_space:
        left_s = end_space.pop(left_e)
        del start_space[left_s]
        invalid.add((left_s - left_e - 1, left_s, left_e))
    else :
        left_s = 0

    if right_s < (n - 1) and start_space:
        right_e = start_space.pop(right_s)
        del end_space[right_e]
        invalid.add((right_s - right_e - 1, right_s, right_e))
    else:
        right_e = mAddr + m_length

    heapq.heappush(heap, (-(right_e - left_s + 1), left_s, right_e))
    # print(f"invalid : {invalid}")

    return m_length
