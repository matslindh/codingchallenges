from bisect import bisect_left
from functools import reduce
from operator import add


def gluewordizer(wordpairs):
    words = [x.strip() for x in open('input/15.wordlist', encoding='utf-8')]
    reverse_words = sorted([word[::-1] for word in words])
    possible = set()

    for prefix, postfix in wordpairs:
        reverse_postfix = postfix[::-1]
        preidx = bisect_left(words, prefix)
        postidx_real = bisect_left(reverse_words, reverse_postfix)

        while words[preidx].startswith(prefix):
            word_prefix = words[preidx]

            if word_prefix == prefix:
                preidx += 1
                continue

            postidx = postidx_real

            while reverse_words[postidx].startswith(reverse_postfix):
                word_postfix = reverse_words[postidx]

                if word_postfix == reverse_postfix:
                    postidx += 1
                    continue

                postsuffix = word_postfix[::-1][0:-len(postfix)]
                presuffix = word_prefix[len(prefix):]

                if presuffix == postsuffix:
                    glue = word_prefix[len(prefix):]

                    if words[bisect_left(words, glue)] == glue:
                        possible.add(glue)

                postidx += 1

            preidx += 1

    return possible


def gluecounter(wordpairs):
    return reduce(add, (len(word) for word in gluewordizer(wordpairs)))


def test_gluecounter():
    assert gluecounter([['innovasjons', 'løsheta'], ['spektral', 'sikringens'], ['verdens', 'spillet']]) == 14


def test_gluewordizer():
    assert gluewordizer([['innovasjons', 'løsheta'], ['spektral', 'sikringens'], ['verdens', 'spillet']]) == {'takt', 'verdi', 'tenor'}


if __name__ == '__main__':
    print(gluecounter([[x.strip() for x in y.split(',')] for y in open('input/15', encoding='utf-8')]))