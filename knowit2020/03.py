def sourcelister(matrix_file):
    matrix = [x.strip() for x in open(matrix_file, encoding='utf-8').readlines()]
    width, height = len(matrix[0]), len(matrix)
    diagonals = []

    # generate diagonals
    for x in range(0, width):
        diagonals.append(diagonal(matrix, x, 0))
        diagonals.append(diagonal(matrix, x, 0, x_d=-1))

    for y in range(0, height):
        diagonals.append(diagonal(matrix, 0, y))
        diagonal(matrix, x, width-1, x_d=-1)

    # generate up/down
    for x in range(0, width):
        s = ''

        for y in range(0, height):
            s += matrix[y][x]

        matrix.append(s)

    matrix += diagonals
    matrix += [x[::-1] for x in matrix]

    return matrix


def diagonal(matrix, x, y, x_d=1):
    width, height = len(matrix[0]), len(matrix)
    d = ''

    while x < width and y < height:
        d += matrix[y][x]
        x += x_d
        y += 1

    return d


def solver(sourcelist, wordlist):
    not_present = []

    for word in wordlist:
        found = False

        for line in sourcelist:
            if word in line:
                found = True
                break

        if not found:
            not_present.append(word)

    return list(sorted(not_present))


def test_diagonal():
    assert 'ad' == diagonal(['ab', 'cd'], 0, 0)
    assert 'b' == diagonal(['ab', 'cd'], 1, 0)
    assert 'c' == diagonal(['ab', 'cd'], 0, 1)


def test_searcher():
    assert ['palmesøndag', 'påskeegg', 'smågodt'] == solver(
        sourcelister('input/03.test'),
        ['kakao', 'kriminalroman', 'kvikklunch', 'kylling', 'langfredag', 'langrennski', 'palmesøndag', 'påskeegg', 'smågodt', 'solvegg', 'yatzy', 'kuas']
    )

    assert ['palmesøndag', 'påskeegg', ] == solver(
        sourcelister('input/03-2.test'),
        ['kakao', 'kriminalroman', 'kvikklunch', 'kylling', 'langfredag', 'langrennski', 'palmesøndag', 'påskeegg', 'smågodt', 'solvegg', 'yatzy']
    )


if __name__ == '__main__':
    print(','.join(solver(
        sourcelister('input/03'),
        """nisseverksted
pepperkake
adventskalender
klementin
krampus
juletre
julestjerne
gløggkos
marsipangris
mandel
sledespor
nordpolen
nellik
pinnekjøtt
svineribbe
lutefisk
medisterkake
grevinne
hovmester
sølvgutt
jesusbarnet
julestrømpe
askepott
rudolf
akevitt""".split("\n")
    )))
