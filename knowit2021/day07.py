ant = 1.0
santa = 20.0
i = 0

while ant < santa:
    ant += ant * 20/santa
    santa += 20
    ant += 1

    if i % 10000000 == 0:
        print(i, santa - ant)

    i += 1

print(ant, santa)