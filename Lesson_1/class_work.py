g = input()
s = input()

x = 137
p = 10 ** 8

g_hash = 0
for symbol in g:
    g_hash *= x
    g_hash += ord(symbol)
    g_hash %= p

w_hash = 0
for symbol in s[:len(g)]:
    w_hash *= x
    w_hash += ord(symbol)
    w_hash %= p
res = []
if g_hash == w_hash:
    res.append(0)
for i in range(1, len(s) - (len(g) - 1)):
    w_hash -= (ord(s[i - 1]) * x ** (len(g) - 1)) % p
    w_hash *= x
    w_hash += ord(s[i + len(g) - 1])
    w_hash %= p

    if g_hash == w_hash:
        res.append(i)

if res:
    print(" ".join([str(x) for x in res]))
else:
    print(-1)



