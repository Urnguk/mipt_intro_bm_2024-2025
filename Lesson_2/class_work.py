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


# A = [2, 7, -2, 8, 0, 4, 13]
# heap_sort(A)
# print(*A)


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.v = value
        self.p = parent
        self.l = left
        self.r = right


class Bin_tree:
    def __init__(self, value):
        self.root = Node(value)


    @classmethod
    def alternative_init(cls, arr):
        A = Bin_tree(arr[0])
        for i in range(1, len(arr)):
            A.add(arr[i])
        return A

    def add(self, value):
        curr_node = self.root
        if value > curr_node.v:
            next_node = curr_node.r
        else:
            next_node = curr_node.l
        while next_node is not None:
            curr_node = next_node
            if value > curr_node.v:
                next_node = curr_node.r
            else:
                next_node = curr_node.l
        if value > curr_node.v:
            curr_node.r = Node(value, curr_node)
        else:
            curr_node.l = Node(value, curr_node)

    def search(self, value):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.v == value:
                return True
            if value > curr_node.v:
                curr_node = curr_node.r
            else:
                curr_node = curr_node.l
        return False

    def _print(self, curr_node):
        if curr_node is None:
            return ""
        return f"{self._print(curr_node.l)} {str(curr_node.v)} {self._print(curr_node.r)}"

    def __str__(self):
        return self._print(self.root)


x = Bin_tree(7)
x.add(5)
x.add(6)
x.add(1)
x.add(9)
print(x)
y = Bin_tree.alternative_init([3, 4, 7])
print(y)



