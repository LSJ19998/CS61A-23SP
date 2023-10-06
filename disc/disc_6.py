def add_this_many(x, el, s):
    count = 0
    for e in s:
        if e == x:
            count += 1
    for _ in range(count):
        s.append(el)


def filter_iter(iterable, f):
    for e in iterable:
        if f(e):
            yield e


def is_prime(n):
    def helper(i):
        # 使用控制语句
        if n == 1:
            return False
        if i == 1:
            return True
        if n % i == 0:
            return False
        else:
            return helper(i - 1)
    return helper(n - 1)


def primes_gen(n):
    while n > 1:
        if is_prime(n):
            yield n
        n -= 1


def primes_gen2(n):
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen2(n - 1)


def preorder(t):
    res = [label(t)]
    if is_leaf(t):
        return res
    for b in branches(t):
        res += preorder(b)
    return res


def generate_preorder(t):
    yield label(t)
    if is_leaf(t):
        return
    for b in branches(t):
        yield from generate_preorder(b)


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be tree'
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_tree(t):
    # 检查类型 |  检车部分抽象
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True


def is_leaf(t):
    return not branches(t)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 1), fib_tree(n - 2)
        root = label(left) + label(right)
        return tree(root, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    return count_leaves(branches(tree)[0]) + count_leaves(branches(tree)[1])


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    if n < 0 or m == 0:
        return tree(False)
    left = partition_tree(n - m, m)
    right = partition_tree(n, m - 1)
    return tree(m, [left, right])


def print_tree(tree, partition=[]):
    if is_leaf(tree):
        print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_tree(left, partition + [m])
        print_tree(right, partition)
