import sys

sys.stdin = open('input.txt', 'r')


def merge(left, right):
    result = []
    left_max_p, right_max_p = len(left), len(right)
    left_p, right_p = 0, 0

    while left_p < left_max_p and right_p < right_max_p:
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1

    for _ in range(left_p, left_max_p):
        result.append(left[left_p])
        left_p += 1

    for _ in range(right_p, right_max_p):
        result.append(right[right_p])
        right_p += 1

    return result


def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


nums = list(map(int, input().split()))



print(merge_sort(nums))
