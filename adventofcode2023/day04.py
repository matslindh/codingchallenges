from typing import List


def numbers(string_of_numbers: str) -> set:
    return set(
        int(number)
        for number in string_of_numbers.split()
    )

def parse_card(line: str):
    card_info, card_numbers = line.split(':')
    expected_s, have_s = card_numbers.split('|')
    expected, have = numbers(expected_s), numbers(have_s)

    return len(expected & have)


def score_card(line: str):
    score = parse_card(line)

    if not score:
        return 0

    return 2 ** (score - 1)


def score_pile(lines: List[str]):
    return sum(
        score_card(line)
        for line in lines
    )


def resulting_number_of_scratchcards(lines: List[str]):
    score_per_card = list(map(parse_card, lines))
    tickets_per_card = [1] * len(score_per_card)

    for idx in range(len(score_per_card) - 1, -1, -1):
        if score_per_card[idx]:
            end_idx = min(len(score_per_card), idx+score_per_card[idx]+1)

            tickets_per_card[idx] += sum(
                tickets_per_card[idx+1:end_idx]
            )

    return sum(tickets_per_card)


def test_resulting_number_of_scratchcards():
    assert resulting_number_of_scratchcards(open("input/04.test").read().splitlines()) == 30


def test_score_pile():
    assert score_pile(open("input/04.test").read().splitlines()) == 13


def test_numbers():
    assert numbers("  1 21 53 59 44") == {1, 21, 53, 59, 44}


def test_parse_card():
    assert parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 4


def test_score_card():
    assert score_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 8
    assert score_card("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == 2
    assert score_card("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == 2
    assert score_card("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == 1
    assert score_card("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == 0
    assert score_card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == 0


if __name__ == '__main__':
    print(score_pile(open("input/04").read().splitlines()))
    print(resulting_number_of_scratchcards(open("input/04").read().splitlines()))