with open("file.txt") as f:
    contents = f.readlines()

def get_numb_game(line:str):
    tmp = ""
    for i in range(len(line)):
        if line[i].isdigit():
            tmp += line[i]
    return int(tmp)

def get_roll_couple(line:str):
    roll_list = []
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    if ";" in line:
        for rolls in line.split(";"):
            for roll in rolls.split(","):
                tmp = ""
                c = 0
                while roll[c].isdigit():
                    tmp+=roll[c]
                    c+=1
                roll_list.append((int(tmp), roll[c:]))
    return roll_list

def nbr_max_cube(rolls:tuple):
    red = []
    blue = []
    green = []
    for roll in rolls:
        if roll[1] == "red":
            red.append(roll[0])
        elif roll[1] == "blue":
            blue.append(roll[0])
        else:
            green.append(roll[0])
    return (max(red), max(blue), max(green))

game_id = 0
power_cube = []
for line in contents:
    game_id = get_numb_game(line.split(":")[0])
    rolls_list = get_roll_couple(line.split(":")[1])
    max_cubes = nbr_max_cube(rolls_list)
    power_cube.append(max_cubes[0]*max_cubes[1]*max_cubes[2])

print(sum(power_cube))
    

