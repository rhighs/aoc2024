import sys

def parse_input(text: str):
    return [[int(v) for v in line.split()] for line in text.splitlines()]

def badpos(r):
    i = 0
    trend = None
    rr = []
    for p, n in zip(r, r[1:]):
        inc = p < n
        if trend is None:
            trend = inc
        elif trend != inc:
            rr.append(i)
            break
        diff = abs(p - n)
        if diff > 3 or diff == 0:
            rr.append(i)
        i += 1
    return rr

def good(r):
    return len(badpos(r)) == 0

def without(r, bp):
    rr = r.copy(); rr.pop(bp); return rr

def semigood(r):
    return any(map(lambda bp: good(without(r, bp)), (bp for bp in range(len(r)))))

def p1(text):
    return sum([1 for r in parse_input(text) if good(r)]) 

def p2(text):
    return sum([1 for r in parse_input(text) if good(r) or semigood(r)]) 

text = sys.stdin.read()
print(p1(text)); print(p2(text))
