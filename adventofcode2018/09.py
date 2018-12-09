def marbles(players, last_marble_worth):
    board = [0]
    board_size = 1
    player = 0
    marble = 1
    placement = 0
    scores = [0] * players

    while True:
        player = (player + 1) % players

        if marble % 23 == 0:
            marble_idx = (placement - 7) % board_size
            popped = board.pop(marble_idx + 1)
            worth = popped + marble
            scores[player] += worth

            #if max(scores) >= 8317:
            #    print(worth, scores, marble)
            #    return

            #if marble == last_marble_worth:
                #return max(scores)

            board_size -= 1

        else:
            marble_idx = (placement + 2) % board_size
            board.insert(marble_idx + 1, marble)
            board_size += 1

        if marble % 10000 == 0:
            print(marble)

        if marble == last_marble_worth:
            return max(scores)

        placement = marble_idx
        marble += 1


def test_marbles():
    assert 32 == marbles(9, 32)
    assert 8317 == marbles(10, 1618)
    assert 146373 == marbles(13, 7999)
    assert 2764 == marbles(17, 1104)
    assert 54718 == marbles(21, 6111)
    assert 37305 == marbles(30, 5807)


if __name__ == '__main__':
    print(marbles(428, 72061))
    print(marbles(428, 7206100))
