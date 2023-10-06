def convert_link(link):
    s = []
    # 返回数据的情况
    if link is Link.empty:
        return s
    # 处理数据的情况
    else:
        s += [link.first] + convert_link(link.rest)
    return s


def duplicate_link(link, val):
    if link is Link.empty:
        return
    if link.first == val:
        new_link = Link(link.first, link.rest)
        link.rest = new_link
        duplicate_link(new_link.rest, val)
    else:
        duplicate_link(link.rest, val)


def multiply_lnks(lst_of_lnks):
    if True in [lns is Link.empty for lns in lst_of_lnks]:
        return Link.empty
    first = 1
    for lst in lst_of_lnks:
        first *= lst.first
    return Link(first, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))


# 考虑的情况
def flip_two(s):
    '''
    if s is Link.empty or s.rest is Link.empty:
        return
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)
    '''
    while s.rest is not Link.empty:
        s.rest.first, s.first = s.first, s.rest.first
        s = s.rest.rest
        if s is Link.empty:
            return


def rey(finn):
    poe = 0
    count = 0
    while finn >= 2:
        poe += finn
        finn /= 2
        count += 1
    return count


def mod_7(n):
    if n % 7 == 0:
        return 0
    else:
        return 1 + mod_7(n-1)


def mod(f):
    def func(n):
        func.time_count += 1
        return f(n)
    func.time_count = 0
    return func

# 需要考虑一下


def find_paths(t, entry):
    if label(t) == entry:
        return [[entry]]
    res = []
    for b in branches(t):
        res.extend([[label(t)] + path for path in find_paths(b, entry)])
    return res


class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


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
