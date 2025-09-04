import heapq

heap = []           # 빈공간: (-길이, 시작, 끝)
start_space = {}    # 시작 → 끝
end_space = {}      # 끝 → 시작
buildings = {}      # 빌딩 시작주소 → 끝주소
invalid = set()     # 힙에서 무시해야 하는 구간


def init(N):
    """토지 초기화"""
    global heap, start_space, end_space, buildings, invalid
    heap = [(-N, 0, N - 1)]
    start_space = {0: N - 1}
    end_space = {N - 1: 0}
    buildings = {}
    invalid = set()


def _valid(s, e):
    """(s,e)가 현재 딕셔너리와 일치하는 유효 구간인지"""
    return start_space.get(s) == e and end_space.get(e) == s


def build(mLength):
    global heap, start_space, end_space, buildings, invalid

    while heap:
        neg_len, s, e = heapq.heappop(heap)
        length = -neg_len

        if (s, e) in invalid:
            invalid.remove((s, e))
            continue
        if not _valid(s, e):
            continue

        if length < mLength:
            return -1

        remain = length - mLength
        right = remain // 2
        left = remain - right
        addr = s + left
        end_b = addr + mLength - 1

        start_space.pop(s, None)
        end_space.pop(e, None)

        buildings[addr] = end_b

        if left > 0:
            ns, ne = s, addr - 1
            start_space[ns] = ne
            end_space[ne] = ns
            heapq.heappush(heap, (-(ne - ns + 1), ns, ne))

        if right > 0:
            ns, ne = end_b + 1, e
            start_space[ns] = ne
            end_space[ne] = ns
            heapq.heappush(heap, (-(ne - ns + 1), ns, ne))

        return addr

    return -1



def demolish(mAddr):
    global heap, start_space, end_space, buildings, invalid

    if mAddr not in buildings:
        return -1

    end_b = buildings.pop(mAddr)
    length = end_b - mAddr + 1

    ns, ne = mAddr, end_b

    # 왼쪽 병합
    left_end = mAddr - 1
    if left_end in end_space:
        ls = end_space.pop(left_end)
        start_space.pop(ls, None)
        invalid.add((ls, left_end))
        ns = ls

    # 오른쪽 병합
    right_start = end_b + 1
    if right_start in start_space:
        re = start_space.pop(right_start)
        end_space.pop(re, None)
        invalid.add((right_start, re))
        ne = re

    # 새 구간 추가
    start_space[ns] = ne
    end_space[ne] = ns
    heapq.heappush(heap, (-(ne - ns + 1), ns, ne))

    return length
