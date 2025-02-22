def heap_add(arr, x):
    arr.append(x)
    j = len(arr) - 1
    while j > 0:
        p = (j - 1) // 2
        if arr[j] > arr[p]:
            arr[j], arr[p] = arr[p], arr[j]
            j = p
        else:
            break
    return


def heap_pop(arr):
    res = arr[0]
    if len(arr) == 1:
        return arr.pop()
    arr[0] = arr.pop()
    j = 0
    while True:
        l = 2 * j + 1
        r = 2 * j + 2
        if l >= len(arr):
            break
        if r >= len(arr):
            if arr[j] < arr[l]:
                arr[j], arr[l] = arr[l], arr[j]
            break
        if arr[j] >= max(arr[l], arr[r]):
            break
        b = l if arr[l] >= arr[r] else r
        arr[j], arr[b] = arr[b], arr[j]
        j = b
    return res

# def heap_pop(A):
#     res = A[0]
#     if len(A) == 1:
#         return res
#     A[0] = A.pop()
#     i = 0
#     j = 2 * i + 1
#     k = 2 * i + 2
#     while j < len(A):
#         c = j
#         if k < len(A) and A[j] > A[k]:
#             c = k
#         if A[i] > A[c]:
#             A[i], A[c] = A[c], A[i]
#             i = c
#         else:
#             break
#         j = 2 * i + 1
#         k = 2 * i + 2
#     return res

def heap_sort(A):
    B = []
    for element in A:
        heap_add(B, element)
    for i in range(len(A)):
        A[len(A) - i - 1] = heap_pop(B)


A = [2, 7, -2, 8, 0, 4, 13]
heap_sort(A)
print(*A)


