from collections import Counter


def lookify(w):
    c = Counter(w)
    return ''.join(sorted(c.keys()))


def ngram(n, w):
    tokens = ''
    i = 0
    lw = len(w)

    while True:
        print(w[i:i+n])
        tokens += w[i:i+n]
        i += 1

        if i+n > lw:
            break

    return tokens


dictionary = open("input/wordlist.txt").readlines()
#dictionary = ['snowflake', 'mistletoe']

lookup = {}

for word in dictionary:
    l = lookify(word.strip())

    if l not in lookup:
        lookup[l] = []

    lookup[l].append(word.strip())


def find_solution(question):
    k = lookify(question)

    for w in lookup[k]:
        c = sorted(question)

        for n in range(2, 10):
            a = sorted(ngram(n, w))

            if a == c:
                return str(n) + '-' + w


def test_ngram():
    assert 'misiststltleletetotoe' == ngram(3, 'mistletoe')
    assert 'snnoowwffllaakke' == ngram(2, 'snowflake')


def test_solution():
    assert '2-snowflake' == find_solution('fnaewkfonklsawlo')
    assert '3-mistletoe' == find_solution('itseotltmlelteoitetss')


print(find_solution('aeteesasrsssstaesersrrsse'))