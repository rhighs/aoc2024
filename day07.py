import sys
from functools import reduce
from itertools import product


def parse_input(text):
    result = []
    for l in text.splitlines():
        c = l.split(": ")
        result.append((int(c[0]), [int(x) for x in c[1].split()]))
    return result


def bits(n, num_len):
    o = list(map(int, bin(n)[2:]))
    return ([0] * (num_len - len(o))) + o


def _solve(tgt, nums, _ops=[]):
    for ops in (list(l) for l in product(_ops, repeat=len(nums))):
        if (
            reduce(
                lambda acc, k: ops[k](acc, nums[k + 1]), range(len(ops) - 1), nums[0]
            )
            == tgt
        ):
            return tgt
    return 0


def p1(text):
    return sum(
        _solve(tgt, nums, _ops=[int.__add__, int.__mul__])
        for tgt, nums in parse_input(text)
    )


def p2(text):
    return sum(
        _solve(
            tgt,
            nums,
            _ops=[int.__add__, int.__mul__, lambda a, b: int(str(a) + str(b))],
        )
        for tgt, nums in parse_input(text)
    )


t = sys.stdin.read()
print(p1(t))
print(p2(t))
