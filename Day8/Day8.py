with open('Day8.txt') as f:
    lines = [l.strip().split('|') for l in f]
    lines = [(ref.split(), output.split()) for ref, output in lines]


# Part One

print(sum(1 for l in lines for o in l[1] if len(o) in [2, 4, 3, 7]))


# Part Two

def solve(mixed, output):
    digits = 10 * [None]
    mixed = [set(d) for d in mixed]

    digits[1] = next(d for d in mixed if len(d) == 2)
    digits[4] = next(d for d in mixed if len(d) == 4)
    digits[7] = next(d for d in mixed if len(d) == 3)
    digits[8] = next(d for d in mixed if len(d) == 7)

    digits[3] = next(d for d in mixed if len(d)==5 and d > digits[1])
    digits[9] = next(d for d in mixed if len(d)==6 and d > digits[3])
    digits[0] = next(d for d in mixed if len(d)==6 and d not in digits and d > digits[1])
    digits[6] = next(d for d in mixed if len(d)==6 and d not in digits)
    digits[5] = next(d for d in mixed if len(d)==5 and d < digits[6])
    digits[2] = next(d for d in mixed if len(d)==5 and d not in digits)

    output = [set(d) for d in output]
    out = 0
    for o in output:
        out = out*10 + next(i for i,d in enumerate(digits) if o == d)
    return out

print(sum(solve(m, o) for m, o in lines))