status = {'thief': True, 'wizard': True, 'warrior': True, 'priest': True}
permadeath = {'wizard': False, 'warrior': False}
survivor_goblins = 0


for room in range(1, 101):
    reanimated = False
    goblins = room

    while True:
        if status['thief']:
            goblins -= 1

        if status['wizard']:
            goblins -= 10

        if status['warrior']:
            goblins -= 1

        if status['priest'] and not reanimated:
            reanimated = True

            if not status['warrior'] and not permadeath['warrior']:
                status['warrior'] = True
            elif not status['wizard'] and not permadeath['wizard']:
                status['wizard'] = True
            else:
                reanimated = False

        if status['thief'] and not status['wizard'] and not status['warrior'] and not status['priest']:
            survivor_goblins += goblins
            break

        adventurers = sum([int(x[1]) for x in status.items()])

        if goblins > 0 and adventurers * 10 <= goblins:
            if status['warrior']:
                status['warrior'] = False
            elif status['wizard']:
                status['wizard'] = False
            elif status['priest']:
                status['priest'] = False

        if goblins < 1:
            break

    if not status['warrior']:
        permadeath['warrior'] = True
    elif not status['wizard']:
        permadeath['wizard'] = True


party_members = sum([int(x[1]) for x in status.items()])
print("survived goblins: " + str(survivor_goblins))
print("survived party members: " + str(party_members))
print("saved people: 17")
print("total: " + str(survivor_goblins + 17 + party_members))



