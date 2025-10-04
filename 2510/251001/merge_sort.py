# def merge(left, right):
#     result = []
#
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#
#     result.extend(left)
#     result.extend(right)
#     print(f"merge 함수 : {result}")
#     return result
#
#
# def merge_sort(arr):
#     n = len(arr)
#
#     if n <= 1:
#         print(f"하나로 분리 : {arr}")
#         return arr
#
#     mid = n // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     print(f"merge_sort 전 left_half : {left_half}")
#     print(f"merge_sort 전 right_half : {right_half}")
#
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#
#     print(f"merge_sort 후 left_half : {left_half}")
#     print(f"merge_sort 후 right_half : {right_half}")
#
#     return merge(left_half, right_half)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)
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


nums = [4, 2, 3, 6, 8, 32, 74, 10, 0]
print(merge_sort(nums))
