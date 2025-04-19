# def moves(n):
#     res = [n - i for i in (1, 2, 3)]
#     if n % 3 == 0:
#         res.pop()
#     elif n % 3 == 1:
#         res.pop(1)
#     return [x for x in res if x >= 0]
#
#
# def Grandi(n, cache=None):
#     if cache is None:
#         cache = dict()
#     if n not in cache:
#         m = moves(n)
#         if len(m) == 0:
#             cache[n] = 0
#         else:
#             children = set()
#             for move in m:
#                 children.add(Grandi(move, cache))
#             res = n
#             for i in range(n):
#                 if i not in children:
#                     res = i
#                     break
#             cache[n] = res
#     return cache[n]
#
#
# x = int(input())
# g = Grandi(x)
# if g > 0:
#     print(1)
# else:
#     print(2)


def moves(n, k):
    res = [n - 1 - i for i in range(k)]
    return [x for x in res if x >= 0]


def Grandi(n, k, cache):
    if n not in cache:
        m = moves(n, k)
        if len(m) == 0:
            cache[n] = 0
        else:
            children = set()
            for move in m:
                children.add(Grandi(move, k, cache))
            res = n
            for i in range(n):
                if i not in children:
                    res = i
                    break
            cache[n] = res
    return cache[n]


def Multi_Grandi(games, k, cache=None):
    if cache is None:
        cache = dict()
    res = Grandi(games[0], k, cache)
    for i in range(1, len(games)):
        res ^= Grandi(games[i], k, cache)
    return res


n, k = [int(x) for x in input().split()]
games = [int(x) for x in input().split()]
if Multi_Grandi(games, k) > 0:
    print("YES")
else:
    print("NO")


