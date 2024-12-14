import sys
from math import gcd


def parse_input(text):
    return [list(l) for l in text.splitlines()]


def simplify(p):
    d = gcd(abs(p[0]), abs(p[1]))
    return p[0] // d, p[1] // d


def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


def sub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


def mul(p1, m):
    return p1[0] * m, p1[1] * m


def in_bounds(g, pos):
    return pos[0] < len(g) and pos[0] >= 0 and pos[1] < len(g[0]) and pos[1] >= 0


def find_pairs(g):
    a = []
    result = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] != ".":
                a.append(((i, j), g[i][j]))
    for (ii, jj), freq in a:
        for i in range(len(g)):
            for j in range(len(g[i])):
                if i == ii and j == jj:
                    continue
                if g[i][j] == freq:
                    dir = (i - ii, j - jj)
                    result.append((((ii, jj), (i, j)), dir))
    return result


def p1(text):
    g = parse_input(text)
    pairs = find_pairs(g)
    antinodes = set()
    for (p1, _), dir in pairs:
        a1, a2 = add(p1, mul(dir, 2)), sub(p1, dir)
        if in_bounds(g, a1):
            antinodes.add(a1)
        if in_bounds(g, a2):
            antinodes.add(a2)
    # for a in antinodes:
    #     if g[a[0]][a[1]] == ".":
    #         g[a[0]][a[1]] = "#"
    # print("\n".join(["".join(x) for x in g]))
    return len(antinodes)


def p2(text):
    g = parse_input(text)
    pairs = find_pairs(g)
    antinodes = set()
    for (p1, _), dir in pairs:
        ndir = simplify(dir)
        i = 1
        while True:
            a1, a2 = add(p1, mul(ndir, i)), sub(p1, mul(ndir, i))
            if not (in_bounds(g, a1) or in_bounds(g, a2)):
                break
            if in_bounds(g, a1):
                antinodes.add(a1)
            if in_bounds(g, a2):
                antinodes.add(a2)
            i += 1
    # for a in antinodes:
    #     if g[a[0]][a[1]] == ".":
    #         g[a[0]][a[1]] = "#"
    # print("\n".join(["".join(x) for x in g]))
    return len(antinodes)


t = sys.stdin.read()
print(p1(t)); print(p2(t))
