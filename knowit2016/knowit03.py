persons = {}

def init_person(person):
    if not person in persons:
        persons[person] = {
            'hates': {},
            'is_hated_by': {},
            'friends': {},
        }


for line in open("input/knowit03").readlines():
    parts = line.strip().split()

    if parts[0] == 'friends':
        init_person(parts[1])
        init_person(parts[2])

        persons[parts[1]]['friends'][parts[2]] = True
        persons[parts[2]]['friends'][parts[1]] = True
    elif parts[1] == 'hates':
        init_person(parts[0])
        init_person(parts[2])
        persons[parts[0]]['hates'][parts[2]] = True
        persons[parts[2]]['is_hated_by'][parts[0]] = True
    else:
        print("Invalid line? " + line)

most_kameos = 0
leader = None

for person in persons:
    stats = persons[person]
    cnt = 0

    for p in stats['hates']:
        if p not in stats['friends']:
            continue

        if p in stats['is_hated_by']:
            continue

        cnt += 1

    if cnt > most_kameos:
        most_kameos = cnt
        leader = person
    elif cnt == most_kameos:
        print("duplicate most: " + str(cnt))

print("Most kameos: " + leader + " (" + str(most_kameos) + ")")