import bisect

lines = open("input/01-dictionary.txt").read().splitlines()
d = {}

for line in lines:
    term, transl = line.split(",")
    d[term] = transl

terms = sorted(d.keys())

inp = open("input/01-letter.txt").read()
out = []
idx = 1

while inp:
    loc = bisect.bisect_left(terms, inp)

    while not inp.startswith(terms[loc]):
        loc -= 1

    t = terms[loc]
    out.append(t)
    inp = inp[len(t):]

terms = [d[t] for t in out]
print(terms)
print(sum(len(term) for term in terms) + len(terms) - 1)