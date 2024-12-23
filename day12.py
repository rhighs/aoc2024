import sys
from functools import reduce
from itertools import chain


def parse_input(text: str):
    return [list(c for c in line) for line in text.splitlines()]


def syms(m):
    return set(chain.from_iterable(m))


def in_bounds(g, pos):
    return pos[0] < len(g) and pos[0] >= 0 and pos[1] < len(g[0]) and pos[1] >= 0


def vlen(v):
    return sum(x**2 for x in v) ** 0.5


def find_areas(m, sym):
    areas = []

    def _start_pos(ii, jj, func):
        first_iter = True
        for i in range(ii, len(m)):
            for j in range(jj if first_iter else 0, len(m[i])):
                first_iter = False
                if func(i, j):
                    return i, j
        return None

    def _area_from(pos):
        area_pos = set([pos])
        q = [pos]
        while q:
            cur = q.pop(0)
            if cur:
                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    n = (cur[0] + dir[0], cur[1] + dir[1])
                    if in_bounds(m, n) and m[n[0]][n[1]] == sym and n not in area_pos:
                        area_pos.add(n)
                        q.append(n)
        return area_pos

    pos = _start_pos(0, 0, lambda i, j: m[i][j] == sym)
    while True:
        area = _area_from(pos)
        areas.append(area)
        pos = _start_pos(
            pos[0],
            pos[1],
            lambda i, j: m[i][j] == sym and not any(map(lambda a: (i, j) in a, areas)),
        )
        if pos is None:
            break
    return (list(a) for a in areas)


def _calc_perimiter(m, start_pos, sym):
    p = 0
    v = set()
    q = [start_pos]
    while q:
        cur = q.pop(0)
        if cur and cur not in v:
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n = (cur[0] + dir[0], cur[1] + dir[1])
                if in_bounds(m, n):
                    if m[n[0]][n[1]] != sym:
                        p += 1
                    else:
                        q.append(n)
                else:
                    p += 1
            v.add(cur)
    return p


def _calc_sides(m, start_pos, sym):
    v = set()
    q = [start_pos]
    xsidesleft, xsidesright, ysidesdown, ysidesup = {}, {}, {}, {}
    while q:
        cur = q.pop(0)
        if cur and cur not in v:
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n = (cur[0] + dir[0], cur[1] + dir[1])
                if in_bounds(m, n):
                    if m[n[0]][n[1]] != sym:
                        if dir[0] == 1:
                            ysidesdown.setdefault(n[0], []).append(n[1])
                        if dir[0] == -1:
                            ysidesup.setdefault(n[0], []).append(n[1])
                        if dir[1] == 1:
                            xsidesright.setdefault(n[1], []).append(n[0])
                        if dir[1] == -1:
                            xsidesleft.setdefault(n[1], []).append(n[0])
                    else:
                        q.append(n)
                else:
                    if dir[0] == 1:
                        ysidesdown.setdefault(n[0], []).append(n[1])
                    if dir[0] == -1:
                        ysidesup.setdefault(n[0], []).append(n[1])
                    if dir[1] == 1:
                        xsidesright.setdefault(n[1], []).append(n[0])
                    if dir[1] == -1:
                        xsidesleft.setdefault(n[1], []).append(n[0])
            v.add(cur)
    return sum(
        (
            sum(
                map(
                    lambda i: 1 if (arr[i] != arr[i - 1] + 1) else 0, range(1, len(arr))
                )
            )
            + 1
        )
        for arr in (
            sorted(v)
            for v in chain.from_iterable(
                x.values() for x in [xsidesleft, xsidesright, ysidesdown, ysidesup]
            )
        )
    )


def p1(text):
    m = parse_input(text)
    return reduce(
        lambda acc, a: acc + (_calc_perimiter(m, a[0], m[a[0][0]][a[0][1]]) * len(a)),
        (a for s in syms(m) for a in find_areas(m, s)),
        0,
    )


def p2(text):
    m = parse_input(text)
    return reduce(
        lambda acc, a: acc + (_calc_sides(m, a[0], m[a[0][0]][a[0][1]]) * len(a)),
        (a for s in syms(m) for a in find_areas(m, s)),
        0,
    )


t = sys.stdin.read()
print(p1(t))
print(p2(t))
