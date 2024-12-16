import sys
from collections import Counter

def parse_input(text: str):
    return [list(map(int, (c for c in line))) for line in text.splitlines()]

def findth(m):
    return list(filter(lambda yx: not m[yx[0]][yx[1]], ((y, x) for y, r in enumerate(m) for x, c in enumerate(r))))

def in_bounds(g, pos):
    return pos[0] < len(g) and pos[0] >= 0 and pos[1] < len(g[0]) and pos[1] >= 0

def solve(m):
    th = findth(m); q = [(t, None) for t in th]; qp = {t: [] for t in th}
    while q:
        cur, p = q.pop(0)
        i, j = cur
        if m[i][j] != 9:
            for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n = (i + di, j + dj)
                ii, jj = n
                if in_bounds(m, n) and m[ii][jj] - m[i][j] == 1:
                    q.append((n, p if p is not None else cur))
        else:
            qp[p].append(cur)
    return qp.values()

def p1(text):
    return sum(map(lambda v: len(set(v)), solve(parse_input(text))))

def p2(text):
    return sum(map(lambda v: len(v), solve(parse_input(text))))

t = sys.stdin.read()
print(p1(t)); print(p2(t))
