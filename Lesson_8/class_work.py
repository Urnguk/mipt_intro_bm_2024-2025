# try:
#     x = int(input())
#     print(1 / x)
#     # raise EOFError
# except ArithmeticError:
#     print("don't divide by zero")
# except ValueError:
#     print("incorrect value")
# else:
#     print("everything correct")
# finally:
#     print("program ended")


# A = [3, 8, -2, 4]
# it = iter(A)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# try:
#     while True:
#         x = next(it)
#         print(x)
# except StopIteration:
#     pass


# def fib():
#     a, b = 1, 1
#     for i in range(2):
#         yield 1
#     while True:
#         a, b = b, a + b
#         yield b


# def my_range(start, finish=None, step=1):
#     if finish is None:
#         start, finish = 0, start
#     curr = start
#     while 0 < (finish - curr) * step:
#         yield curr
#         curr += step


# for i in my_range(12, 2, 0):
#     print(i)

# cnt = 0
# for f in fib():
#     print(f)
#     cnt += 1
#     if cnt == 100:
#         break

from functools import cache


def time_decor(func):
    import time

    def decorated_func(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        finish_time = time.time()
        return res, finish_time - start_time

    return decorated_func


# @time_decor
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


fib = time_decor(fib)


# c = 3
# print(fib(12000))

# def super_test(a):
#     c = 1
#     test(a)
#
#
# def test(a):
#     print(a)
#     print(c)
#
#
# a = 5
# c = 3
# super_test(2)
