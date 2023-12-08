from collections import Counter


card_priority = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
card_priority_wildcard = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')


def score_hand_wildcards(hand):
    if not 'J' in hand:
        return score_hand(hand)

    cards = set(hand)
    cards.remove('J')

    if len(cards) == 0:
        return score_hand("AAAAA")

    return max(
        score_hand(hand.replace('J', card))
        for card in cards
    )


def score_hand(hand):
    counts = Counter(hand).values()

    # high card
    if len(counts) == 5:
        return 0

    # pair
    if len(counts) == 4:
        return 1

    if len(counts) == 3:
        # two pair
        if 2 in counts:
            return 2
        # three of a kind
        else:
            return 3

    if len(counts) == 2:
        # full house
        if 2 in counts:
            return 4
        # four of a kind
        else:
            return 5

    return 6


def comparable_hand(hand, hand_scorer=score_hand, priority=card_priority):
    return (
        hand_scorer(hand),
        priority.index(hand[0]),
        priority.index(hand[1]),
        priority.index(hand[2]),
        priority.index(hand[3]),
        priority.index(hand[4]),
    )


def sort_hands(hands):
    return tuple(sorted(hands, key=lambda hand: comparable_hand(hand[0])))


def sort_hands_wildcard(hands):
    return tuple(sorted(hands,
                        key=lambda hand: comparable_hand(hand[0],
                                                         hand_scorer=score_hand_wildcards,
                                                         priority=card_priority_wildcard,
                                                         )))


def total_winnings(hands, hand_sorter=sort_hands):
    sorted_hands = hand_sorter(hands)

    return sum(
        (idx + 1) * hand_bet[1]
        for idx, hand_bet in enumerate(sorted_hands)
    )


def parse_hands(lines):
    hands = []

    for line in lines:
        hand, bet = line.split()
        hands.append((hand, int(bet)))

    return hands


def test_parse_hands():
    assert parse_hands(open("input/07.test").read().splitlines()) == [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]


def test_total_winnings():
    hands = [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]

    assert total_winnings(hands) == 6440


def test_total_winnings_wildcards():
    hands = [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]

    assert total_winnings(hands, hand_sorter=sort_hands_wildcard) == 5905


def test_sort_hands():
    hands = [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]

    assert sort_hands(hands) == (
        ("32T3K", 765),
        ("KTJJT", 220),
        ("KK677", 28),
        ("T55J5", 684),
        ("QQQJA", 483),
    )


def test_score_hand():
    assert score_hand("32T3K") == 1
    assert score_hand("T55J5") == 3
    assert score_hand("KK677") == 2
    assert score_hand("KTJJT") == 2
    assert score_hand("QQQJA") == 3

    assert score_hand("12345") == 0
    assert score_hand("55AAA") == 4
    assert score_hand("5AAAA") == 5
    assert score_hand("AAAAA") == 6


if __name__ == "__main__":
    hands = parse_hands(open("input/07").read().splitlines())
    print(total_winnings(hands))
    print(total_winnings(hands, hand_sorter=sort_hands_wildcard))