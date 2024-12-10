import sys

def parse_input(text):
    return [list(l) for l in text.splitlines()]

def is_guard(g, p):
    return g[p[1]][p[0]] == '>' or g[p[1]][p[0]] == 'v' or g[p[1]][p[0]] == '<' or g[p[1]][p[0]] == '^'

def rot(v):
    if v == '>': return 'v'
    if v == 'v': return '<'
    if v == '<': return '^'
    if v == '^': return '>'

def dir(v):
    if v == '>': return 1,  0
    if v == 'v': return 0,  1
    if v == '<': return -1, 0
    if v == '^': return 0, -1

def navigate(g, obs=None):
    s = set()
    sd = set()
    for y in range(len(g)):
        for x in range(len(g[y])):
            if is_guard(g, (x, y)):
                ix, iy = x, y
    init = g[iy][ix]
    x, y = ix, iy
    dx, dy = dir(g[y][x])
    shape = init
    while True:
        s.add((x, y))
        sd.add((x, y, dx, dy))
        if x + dx == len(g[0]) or x + dx < 0 or y + dy == len(g) or y + dy < 0:
            break
        if obs != None and y + dy == obs[1] and x + dx == obs[0]:
            shape = rot(shape)
            dx, dy = dir(shape)
        if g[y + dy][x + dx] != '#':
            x += dx
            y += dy
        else:
            shape = rot(shape)
            dx, dy = dir(shape)
        if (x, y, dx, dy) in sd:
            return s, True
    return s, False

def p1(text):
    return len(navigate(parse_input(text))[0])

def p2(text):
    g = parse_input(text)
    return sum(map(int, (navigate(g, obs=(x, y))[1] for x, y in  navigate(g)[0] if not is_guard(g, (x, y)))))

t = sys.stdin.read()
print(p1(t)); print(p2(t))
