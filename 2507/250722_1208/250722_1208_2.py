from collections import deque
INF = 10**3

for tc in range(1, 11):
    dump = int(input())
    nums = deque(sorted(map(int, input().split())))
    lls = deque()
    sli = deque()

    while dump:
        hi = max(nums[-1] if nums else -INF, lls[0] if lls else -INF)#이건 max([nums가 남아있다면 nums의 최댓값 없다면 -1000]<둘 중 큰값 구하는> lis가 있다면 lis의 최댓값)
        lo = min(nums[0] if nums else INF,  sli[0] if sli else INF)#이건 빈대로 최솟값
        if hi - lo <= 1:#조기종료
            break
        dump -= 1#연산횟수 감소

        if lls and lls[0] >= (nums[-1] if nums else -INF):
            v = lls.popleft()
        else:
            v = nums.pop()
        v -= 1

        if not lls or v >= lls[0]:
            lls.appendleft(v)
        else:
            lls.append(v)
# 여기까지 최댓값 관리하는 조건
        if sli and sli[0] <= (nums[0] if nums else INF):
            v = sli.popleft()
        else:
            v = nums.popleft()
        v += 1

        if not sli or v <= sli[0]:
            sli.appendleft(v)
        else:
            sli.append(v)
# 여기까지 최솟값 괸리하는 조건문

    hi = max(nums[-1] if nums else -INF, lls[0] if lls else -INF)
    lo = min(nums[0] if nums else INF,  sli[0] if sli else INF)
#한번 더 업데이트 해주고 출력
    print(f"#{tc} {hi - lo}")