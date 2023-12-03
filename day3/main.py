import sys

NUMBER = 0
INDEX_ST = 1
INDEX_EN = 2

def get_data_from_file(input_file):
    with open(input_file) as f:
        data = f.readlines()
    
    return data

def extract_numbers(line):
    numbers = list()
    num = ""
    index = -1
    index_end = -1
    i = 0
    for char in line:
        if char.isdigit():
            num += char
            index_end += 1
            if index == -1:
                index = i
        elif num != "":
            numbers.append([num, index, index+index_end])
            num = ""
            index = -1
            index_end = -1
        i += 1
    return numbers

def extract_stars(line):
    stars = list()
    i = 0
    for char in line:
        if char == "*":
            stars.append(i)
        i += 1
    
    return stars


def check_line(line, number_index, number_len, line_length):
    number_end = number_index+number_len-1
    if number_index == 0:
        start_index = 0
    else:
        start_index = number_index-1
    if number_end == line_length:
        end_index = line_length
    else:
        end_index = number_end+1
    for char in line[start_index:end_index+1]:
        if not char.isdigit() and char != ".":
            return "1"
    return "0"
def solution1(data):
    sum = 0
    line_length = len(data[0].replace("\n",""))
    for i in range(len(data)):
        for number_w_index in extract_numbers(data[i]):
            checks = ""
            number_len = len(number_w_index[NUMBER])
            if i != 0:
                checks += check_line(data[i-1].replace("\n",""), number_w_index[INDEX_ST], number_len, line_length)
            if i != len(data)-1:
                checks += check_line(data[i+1].replace("\n",""), number_w_index[INDEX_ST], number_len, line_length)
            checks += check_line(data[i].replace("\n",""), number_w_index[INDEX_ST], number_len, line_length)
            if "1" in checks:
                sum += int(number_w_index[NUMBER])
    return sum

def solution2(data):
    sum = 0
    #line_length = len(data[0].replace("\n",""))
    number_lines = list()
    for line in data:
        number_lines.append(extract_numbers(line))
    for i in range(len(data)):
        for star_index in extract_stars(data[i]):
            numbers_in_range = list()
            if i != 0:
                for numbers in number_lines[i-1]:
                    if star_index in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index-1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index+1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1):
                        numbers_in_range.append(numbers[NUMBER])
            if i != len(data)-1:
                for numbers in number_lines[i+1]:
                    if star_index in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index-1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index+1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1):
                        numbers_in_range.append(numbers[NUMBER])
            for numbers in number_lines[i]:
                    if star_index in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index-1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1) or star_index+1 in range(numbers[INDEX_ST],numbers[INDEX_EN]+1):
                        numbers_in_range.append(numbers[NUMBER])

            if len(numbers_in_range) == 2:
                sum += int(numbers_in_range[0])*int(numbers_in_range[1])

            
    
    return sum

data = get_data_from_file(str(sys.argv[1]))
res1 = solution1(data)
res2 = solution2(data)

print("Result1: ",res1)
print("Result2: ",res2)
