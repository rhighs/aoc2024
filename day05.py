import sys
from functools import reduce

def parse_input(text: str):
    o, u = text.split('\n\n')
    uu = [list(map(int, k)) for k in (uu.split(',') for uu in u.splitlines())]
    da = {}
    for a, b in ((int(a), int(b)) for a, b in (oo.split('|') for oo in o.splitlines())):
        da.setdefault(b, []).append(a)
    return uu, da

def is_ord(l, da):
    return all(not (l[i] in da and bool(set(l[i+1:]) & set(da[l[i]]))) for i in range(len(l) - 1))

def p1(text):
    u, da = parse_input(text)
    v = filter(lambda l: is_ord(l, da), u)
    return reduce(lambda acc, l: acc + l[(len(l)-1)//2], v, 0)

def p2(text):
    u, da = parse_input(text)
    n = list(filter(lambda l: not is_ord(l, da), u))
    for l in n:
        while not is_ord(l, da):
            for i in range(len(l) - 1):
                if l[i] in da:
                    c = list(set(l[i+1:]) & set(da[l[i]]))
                    if c:
                        f = l.index(c[0]); l[i], l[f] = l[f], l[i]
    return reduce(lambda acc, l: acc + l[(len(l)-1)//2], n, 0)

t = sys.stdin.read()
print(p1(t)); print(p2(t))
