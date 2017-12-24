import copy

def execute(moves):
    players = [
        {'name': 'Xena', 'score': 0}, 
        {'name': 'Ophelia', 'score': 0},
    ]
    idx = 0
    first_player = 0
    draw_count = 0
    move_count = 0
    init_map = [[False]*3, [False]*3, [False]*3]
    map = copy.deepcopy(init_map)

    for move in moves:
        move = int(move)
        player_idx = (idx + first_player) % 2
        player = players[player_idx]
        idx += 1

        row = (move - 1) // 3
        column = (move - 1) % 3

        move_count += 1
        map[row][column] = 'X' if player_idx == first_player else 'O'
            
        done = False

        if (check_winning(map)):
            done = True
            draw_count = 0
            players[player_idx]['score'] += 1
            first_player = 0 if player_idx else 1
            print("win " + str(player_idx))

        elif move_count == 9:
            done = True
            draw_count += 1
            print("draw")
            
            if draw_count == 3:
                print("three draws, resetting")
                draw_count = 0
                first_player = 0 if first_player else 1

        if done:
            idx = 0
            print_map(map)
            move_count = 0
            map = copy.deepcopy(init_map)

    print(players)

def print_map(map):
    for row in map:
        for column in row:
            print(column if column else '.', end='')
            
        print('')
    
    print('')
    
    
def check_winning(map):
    if map[1][1] and map[0][0] == map[1][1] == map[2][2]:
        print("win diag 1")
        return map[0][0]
        
    if map[1][1] and map[0][2] == map[1][1] == map[2][0]:
        print("win diag 2")
        return map[0][2]

    for i in range(0, 3):
        if map[i][0] and map[i][0] == map[i][1] == map[i][2]:
            print("win vertical " + str(i))
            return map[i][0]

        if map[0][i] and map[0][i] == map[1][i] == map[2][i]:
            print("win horizontal " + str(i))
            return map[0][i]

    return None


execute(open("input/dec23").read())
