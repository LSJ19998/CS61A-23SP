def multiply(m, n):
    if n == 1:
        return m
    return m + multiply(m, n - 1)


def skip_mul(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return n * skip_mul(n - 2)


def is_prime(n):
    if n == 1:
        return False

    def helper(i):
        if i == 1:
            return True
        if n % i == 0:
            return False
        return helper(i - 1)
    return helper(n - 1)


def hailstone(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 1:
        return 1 + hailstone(3 * n + 1)
    else:
        return 1 + hailstone(n // 2)


def merge(n1, n2):
    if n1 < 1 and n2 < 1:
        return 0
    if n1 < 1:
        return n2
    if n2 < 1:
        return n1
    if n1 % 10 < n2 % 10:
        return n1 % 10 + 10 * merge(n1 // 10, n2)
    if n1 % 10 > n2 % 10:
        return n2 % 10 + 10 * merge(n1, n2 // 10)
    return n1 % 10 + 10 * (n1 % 10) + 100 * merge(n1 // 10, n2 // 10)
