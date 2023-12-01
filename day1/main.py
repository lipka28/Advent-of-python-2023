import sys

D_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_data_from_file(input_file):
    with open(input_file) as f:
        data = f.readlines()
    
    return data

def analyze1(line):
    first_digit, last_digit = "", ""
    for char in line:
        if char.isdigit():
            if first_digit == "":
                first_digit, last_digit = char, char
            else:
                last_digit = char
    return int("{}{}".format(first_digit, last_digit))

def analyze2(line):
    first_digit, last_digit = "", ""
    line_length = len(line)
    for i in range(line_length):
        digit = None
        if line[i].isdigit():
            digit = line[i]
        else:
            for number_name in D_NUMBERS.keys():
                num_len = len(number_name)
                if i+num_len > line_length:
                    continue
                if number_name in line[i:i+num_len]:
                    digit = D_NUMBERS[number_name]     
        if digit:
            if first_digit == "":
                first_digit, last_digit = digit, digit
            else:
                last_digit = digit
    return int("{}{}".format(first_digit, last_digit))

    pass

def solution1(data):
    sum = 0
    for line in data:
        sum += analyze1(line)
    return sum

def solution2(data):
    sum = 0
    for line in data:
        sum += analyze2(line)
    return sum


data = get_data_from_file(str(sys.argv[1]))
res1 = solution1(data)
res2 = solution2(data)

print("Result 1:",res1)
print("Result 2:",res2)


