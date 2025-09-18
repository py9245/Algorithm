
def ddd(arr, n):
    if n == 3:
        return
    num = arr.pop()
    ddd(arr, n - 1)
    print(num)
    arr.append(num)


A = [1, 2, 3, 4, 5]

ddd(A, 5)
print(A)