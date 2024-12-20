from typing import List


def count_categories_to_keep(lines: List[str]):
    kept = []

    def recurse(idx, level):
        has_gifts = False

        while idx < len(lines):
            if not lines[idx].startswith('-' * level):
                return has_gifts, idx

            current = lines[idx]
            line = current.lstrip('-')

            if line.startswith('G'):
                has_gifts = True
                idx += 1
            elif line.startswith('K'):
                category_has_gifts, idx = recurse(idx + 1, level + 1)

                if category_has_gifts:
                    kept.append(current)

                if not has_gifts:
                    has_gifts = category_has_gifts
            else:
                idx += 1

        return has_gifts, idx

    recurse(0, 0)
    return len(kept)


def test_count_categories_to_keep():
    assert count_categories_to_keep(open('input/12.test', encoding='utf-8').read().splitlines()) == 5
    assert count_categories_to_keep(open('input/12.test2', encoding='utf-8').read().splitlines()) == 5


if __name__ == '__main__':
    print(count_categories_to_keep(open('input/12', encoding='utf-8').read().splitlines()))