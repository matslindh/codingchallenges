inp = 3004953
#inp = 5

elves = []

for i in range(0, inp):
    elves.append({
        'gifts': 1,
        'index': i + 1,
    })

while len(elves) > 1:
    new_elves = []

    for i in range(0, len(elves), 2):
        src = i
        dst = (i+1)%len(elves)

        new_elves.append({
            'gifts': elves[src]['gifts'] + elves[dst]['gifts'],
            'index': elves[src]['index'],
        })

        if dst < src:
            del new_elves[0]

    elves = new_elves

print(elves)
