import sys

def parse_input(text: str):
    return list(map(int, text.split()))

def expand(n, b, mem):
    if b == 0:
        return 1
    else:
        if (n, b) in mem:
            return mem[(n, b)]
        if n == 0:
            r = expand(1, b - 1, mem)
        elif len(str(n)) % 2 == 0:
            ss = str(n)
            r = expand(int(ss[:len(ss)//2]), b - 1, mem) \
                + expand(int(ss[len(ss)//2:]), b - 1, mem)
        else:
            r = expand(n * 2024, b - 1, mem)
        mem[(n, b)] = r
        return r

def p1(text):
    mem = {}; return sum(map(lambda i: expand(i, 25, mem), parse_input(text)))

def p2(text):
    mem = {}; return sum(map(lambda i: expand(i, 75, mem), parse_input(text)))

t = sys.stdin.read()
print(p1(t)); print(p2(t))
