def count_stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    #  结束的情况
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # 执行期间的情况
    i = 1
    sum = 0
    while i <= k:
        sum += count_k(n - i, k)
        i += 1
    return sum

# extra recursion problem


def collapse(n):
    def helper(n, k):
        if n < 1:
            return 0
        elif n % 10 == k:
            return helper(n // 10, n % 10)
        return 10 * helper(n // 10, n % 10) + n % 10
    return helper(n, n % 10 + 1)


def repeat_digits(n):
    last, rest = n // 10, n % 10
    if last < 1:
        return rest + rest * 10
    return 100 * repeat_digits(last) + rest * 10 + rest


def even_weighted_loop(s):
    # return [ s[i] * i for i in range(len(s)) if i % 2 == 0]
    new = []
    for i in range(len(s)):
        if i % 2 == 0:
            new += [i * s[i]]
    return new


def max_product(s):
    if len(s) == 1:
        return s[0]
    if len(s) == 0:
        return 1
    return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))
