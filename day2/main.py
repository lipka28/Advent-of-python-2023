import sys

D_DICE_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_data_from_file(input_file):
    with open(input_file) as f:
        data = f.readlines()
    
    return data

def process_game(game_line):
    game_id, game_data = game_line.split(':')
    game_id = int(game_id.replace("Game ", ""))
    game_rounds = game_data.split(';')
    for game_round in game_rounds:
        d_dice_count = {
            "red": 0,
            "green": 0,
            "blue": 0
            }
        for dice in game_round.split(','):
            count, d_type = dice.strip().split(' ')
            d_dice_count[d_type] += int(count)

        for key in D_DICE_LIMITS.keys():
            if d_dice_count[key] > D_DICE_LIMITS[key]:
                return 0
    
    return game_id

def process_game_v2(game_line):
    d_dice_count = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    game_id, game_data = game_line.split(':')
    game_id = int(game_id.replace("Game ", ""))
    game_rounds = game_data.split(';')
    for game_round in game_rounds:
        for dice in game_round.split(','):
            count, d_type = dice.strip().split(' ')
            if d_dice_count[d_type] < int(count):
                d_dice_count[d_type] = int(count)
    
    return d_dice_count["red"]*d_dice_count["blue"]*d_dice_count["green"]

def solution1(data):
    sum = 0
    for line in data:
        sum += process_game(line)
    return sum

def solution2(data):
    sum = 0
    for line in data:
        sum += process_game_v2(line)
    return sum

data = get_data_from_file(str(sys.argv[1]))
res1 = solution1(data)
res2 = solution2(data)

print("Result 1: ", res1)
print("Result 2: ", res2)
