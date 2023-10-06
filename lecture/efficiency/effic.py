def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def count1(f):
    num = 0
    # 可以使用函数的本地变量
    # 但是难以被取用

    def counted(*args):
        nonlocal num
        num += 1
        return f(*args)

    return counted


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted


def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
            memoized.store_num += 1
        return cache[n]
    memoized.store_num = 0
    return memoized
