ladders = {3: 17, 8: 10, 15: 44, 22: 5, 39: 56, 49: 75, 62: 45, 64: 19, 65: 73, 80: 12, 87: 79}
player_count = 1337
ladders_used = 0
players = [1]*(player_count+1)

dice = open("input/knowit08").readlines()
done = False

while not done:
    for i in range(1, player_count+1):
        players[i] += int(dice.pop(0))

        if players[i] in ladders:
            players[i] = ladders[players[i]]
            ladders_used += 1

        if players[i] == 90:
            print("Winner winner chicken dinner: " + str(i) + " (answer: " + str(i*ladders_used) + ")")
            done = True
            break
