with open("file.txt") as f:
    contents = f.readlines()

numbers_dict = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
numbers = "123456789"

def get_numb(slice:str):
    if slice[0] in numbers:
        return slice[0]
    for number in numbers_dict.keys():
        if slice.startswith(number):
            return numbers_dict[number]
sum = 0
for line in contents:
    first_digit = None
    last_digit = None
    for i, c in enumerate(line):
        slice = line[i:]
        if not first_digit:
            first_digit = get_numb(slice)
        tmp = get_numb(slice)
        if tmp:
            last_digit = tmp
    if not last_digit:
        last_digit = first_digit
    tmp = first_digit+last_digit
    sum += int(tmp)

print(sum)

f.close()