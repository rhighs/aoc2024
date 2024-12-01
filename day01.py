import sys
from collections import Counter

def parse_input(text):
    f, s = [list(k) for k in zip(*[[int(x) for x in line.split() if x.isdigit()] for line in text.splitlines() if line.strip()])]
    return f, s

def p1(text):
    f, s = parse_input(text)
    f.sort(); s.sort()
    return sum([abs(s[i] - f[i]) for i in range(len(s))])

def p2(text):
    f, s = parse_input(text)
    c2 = Counter(s)
    return sum([k * c2[k] for k in f if k in c2])

t = sys.stdin.read()
print(p1(t)); print(p2(t))
