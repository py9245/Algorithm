# import sys
#
# sys.stdin = open('input.txt', 'r')

def partition(arr, start, end):
    p = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= end and arr[left] < p:
            left += 1
        while right > start and arr[right] >= p:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            print(arr)
        else:
            break

    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)

        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


arr = [54, 21, 5, 3, 23, 61, 2, 534, 32, 1]
quick_sort(arr, 0, len(arr) - 1)
# print(arr)