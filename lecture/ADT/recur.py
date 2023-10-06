class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]

    def __len__(self):
        # 到达empty, 停止了
        return 1 + len(self.rest)

    def __repr__(s):
        if s.rest is Link.empty:
            rest = ''
        else:
            rest = repr(s.rest)
        return f'Link({s.first}, {s.rest})'
