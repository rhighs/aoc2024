import sys

def p1(text):
    l = text.splitlines()
    T = "\n".join(["".join(l) for l in zip(*l)])
    p, ap = "XMAS", "SAMX"
    c = text.count(p) + text.count(ap) + T.count(p) + T.count(ap)
    ll, lp = len(l), len(p)
    for i in range(ll - lp + 1):
        for j in range(len(l[i]) - lp + 1):
            c += int(all(l[i+k][j+k] == p[k] for k in range(lp)))
    for i in range(lp - 1, ll):
        for j in range(len(l[i]) - lp + 1):
            c += int(all(l[i-k][j+k] == p[k] for k in range(lp)))
    for i in range(ll - lp + 1):
        for j in range(lp - 1, len(l[i])):
            c += int(all(l[i+k][j-k] == p[k] for k in range(lp)))
    for i in range(lp - 1, ll):
        for j in range(lp - 1, len(l[i])):
            c += int(all(l[i-k][j-k] == p[k] for k in range(lp)))
    return c


def p2(text):
    c = 0
    lines = text.splitlines()
    for i in range(0, len(lines) - 2):
        for j in range(1, len(lines[i]) - 1):
            f = lines[i][j-1:j+2]
            s = lines[i+1][j-1:j+2]
            t = lines[i+2][j-1:j+2]
            c += int(f[0] == "M" and f[2] == "S" and s[1] == "A" and t[0] == "M" and t[2] == "S" \
            or f[0] == "S" and f[2] == "M" and s[1] == "A" and t[0] == "S" and t[2] == "M" \
            or f[0] == "M" and f[2] == "M" and s[1] == "A" and t[0] == "S" and t[2] == "S" \
            or f[0] == "S" and f[2] == "S" and s[1] == "A" and t[0] == "M" and t[2] == "M")
    return c

text = sys.stdin.read()
print(p1(text))
print(p2(text))
