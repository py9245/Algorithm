import heapq

n = 0
heap = []
start_space = {}
end_space = {}
buildings = {}
invalid = set()


def _valid_interval(s, e):
    return start_space.get(s) == e and end_space.get(e) == s


def init(N):
    global n, heap, start_space, end_space, buildings, invalid
    n = N
    heap = [(-(N), 0, N - 1)]
    start_space = {0: N - 1}
    end_space = {N - 1: 0}
    buildings = {}
    invalid = set()


def build(mLength):
    global heap, start_space, end_space, buildings, invalid

    while heap:
        neg_len, s, e = heapq.heappop(heap)

        if (s, e) in invalid:
            invalid.discard((s, e))
            continue

        if start_space.get(s) != e or end_space.get(e) != s or -neg_len != (e - s + 1):
            continue

        length = -neg_len
        if length < mLength:
            heapq.heappush(heap, (neg_len, s, e))
            return -1

        remain = length - mLength
        left_len = remain // 2
        right_len = remain - left_len

        build_id = s + left_len

        del start_space[s]
        del end_space[e]

        buildings[build_id] = mLength

        if left_len > 0:
            left_s = s
            left_e = s + left_len - 1
            start_space[left_s] = left_e
            end_space[left_e] = left_s
            heapq.heappush(heap, (-(left_len), left_s, left_e))

        if right_len > 0:
            right_s = e - right_len + 1
            right_e = e
            start_space[right_s] = right_e
            end_space[right_e] = right_s
            heapq.heappush(heap, (-(right_len), right_s, right_e))

        return build_id

    return -1



def demolish(mAddr):
    global heap, start_space, end_space, buildings, invalid

    if mAddr not in buildings:
        return -1

    m_length = buildings.pop(mAddr)

    left_e = mAddr - 1
    right_s = mAddr + m_length

    left_s = end_space.pop(left_e, None)
    if left_s is not None:
        del start_space[left_s]
        invalid.add((left_s, left_e))
    else:
        left_s = mAddr  # 철거 시작이 새 빈공간 시작

    right_e = start_space.pop(right_s, None)
    if right_e is not None:
        del end_space[right_e]
        invalid.add((right_s, right_e))
    else:
        right_e = mAddr + m_length - 1  # 철거 끝이 새 빈공간 끝

    new_s, new_e = left_s, right_e
    heapq.heappush(heap, (-(new_e - new_s + 1), new_s, new_e))
    start_space[new_s] = new_e
    end_space[new_e] = new_s

    return m_length
