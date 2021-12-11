import time
from collections import defaultdict


def decrypt_lists(encoded_names, names):
    gifts = defaultdict(lambda: 0)
    name_sets = {}

    for name in names:
        name_sets[name] = set(name)

    for encoded in encoded_names:
        possible = []
        encoded_set = set(encoded)

        for name in names:
            # speedup 4x
            if not name_sets[name] <= encoded_set:
                continue

            decrypted = decrypter(encoded, name)

            if decrypted:
                possible.append((decrypted, name))

        if possible:
            if len(possible) == 1:
                gifts[possible[0][1]] += 1
            else:
                s_possible = sorted(possible)
                if s_possible[0][0][0] != s_possible[1][0][0]:
                    gifts[s_possible[0][1]] += 1

    print(sorted(gifts.items(), key=lambda x: x[1], reverse=True))


def decrypter(encrypted, search):
    found = []

    def decrypt(idx, left, current, can_flip):
        if not left:
            found.append((current, encrypted.find(current[0]), idx))
            return

        if idx >= len(encrypted):
            return

        next_idx = encrypted.find(left[0], idx)

        if next_idx > -1:
            decrypt(next_idx + 1, left[1:], current + left[0], can_flip)

        if can_flip and len(left) > 1:
            next_idx = encrypted.find(left[1], idx)

            if next_idx > -1:
                decrypt(next_idx + 1, left[0] + (left[2:] if len(left) > 2 else ''), current + left[1], False)

    decrypt(0, search, '', True)

    if found:
        best = None

        for matched, first_idx, last_idx in found:
            length = last_idx - first_idx

            if not best or length < best:
                best = length

        return best - len(search), best

    return None


def test_decrypter():
    assert decrypter('xuabcfglxvuabcflxz', 'alvulf') == (8, 14)


if __name__ == '__main__':
    start = time.time()
    decrypt_lists(open('input/11').read().splitlines(), open('input/11.names').read().splitlines())
    print(time.time() - start)
