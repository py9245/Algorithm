import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    def merge(left, right):
        global cnt

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        if i < len(left):
            cnt += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    def merge_sort(arr):
        n = len(arr)

        if n <= 1:
            return arr

        mid = n // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

        return merge(left_arr, right_arr)


    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    sorted_nums = merge_sort(nums)

    print(f"#{tc} {sorted_nums[N // 2]} {cnt}")