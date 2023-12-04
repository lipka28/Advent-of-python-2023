import sys

POINTS = 0
COUNT = 1

def get_data_from_file(input_file):
    with open(input_file) as f:
        data = f.readlines()
    
    return data

def split_to_numbers(line):
    win_numbers, numbers = list(), list()
    rough_numbers = line.split(':')[1].strip()
    for win_number in rough_numbers.split('|')[0].split(" "):
        if win_number.isnumeric():
            win_numbers.append(int(win_number))
    for number in rough_numbers.split('|')[1].split(" "):
        if number.isnumeric():
            numbers.append(int(number))
    return win_numbers, numbers

def calculate_points(num):
    if num <= 1:
        return num
    return pow(2, num-1)

def solution1(data):
    sum = 0
    line_num = 1
    for line in data:
        points = 0
        win_nums, nums = split_to_numbers(line)
        for num in nums:
            if num in win_nums:
                points += 1
        sum += calculate_points(points)
        line_num += 1
    return sum

def solution2(data):
    sum = 0
    card_list = list()
    for line in data:
        points = 0
        win_nums, nums = split_to_numbers(line)
        for num in nums:
            if num in win_nums:
                points += 1
        card_list.append([points, 1])

    for i in range(len(card_list)):
        wins = card_list[i][POINTS]
        for card_index in range(i, i+wins):
            card_list[card_index+1][COUNT] += card_list[i][COUNT]

    for card in card_list:
        sum += card[COUNT]
    return sum

data = get_data_from_file(str(sys.argv[1]))
res1 = solution1(data)
res2 = solution2(data)

print("Result1: ",res1)
print("Result2: ",res2)
