import sys
import re
from functools import reduce

def _eval(mem):
    return reduce(
        lambda x, f: x + (f[0] * f[1]),
        (list(map(int, re.findall(r"\d+", m))) for m in re.findall(r"mul\(\d+,\d+\)", mem)),
        0,
    )

def p1(m):
    return _eval(m)

def p2(m):
    return _eval("".join(list(map(lambda b: b.split("don't()")[0], m.split("do()")))))

text = sys.stdin.read()
print(p1(text)); print(p2(text))
