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
