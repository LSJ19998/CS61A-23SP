from operator import add


def height(t):
    # 如何假想数据
    if is_leaf(t):
        return 0
    return max([1 + height(b) for b in branches(t)])


def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    return max([label(t) + max_path_sum(b) for b in branches(t)])


def find_path(t, x):
    if is_leaf(t):
        return [label(t)]
    for b in branches(t):
        res = [label(t)] + find_path(b, x)
        if x in res:
            return res
    return


def sum_tree(t):
    return label(t) + sum([sum_tree(b) for b in branches(t)])


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    if is_leaf(t):
        # 建立意义
        return [True]
    first = sum_tree(branches(t)[0])
    res = []
    for b in branches(t):
        if first == sum_tree(b):
            res += [True and balanced(b)]
        else:
            res += [False]
    return False not in res


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(b) for b in leaves])
    return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])


def print_tree(t):
    def helper_print(t, s):
        if is_leaf(t):
            print(s + str(label(t)))
            return
        print(s + str(label(t)))
        for b in branches(t):
            helper_print(b, s + " ")
    return helper_print(t, "")


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
