# write your code here
cells = list("_________")
cells = [[cells[i], cells[i + 1], cells[i + 2]] for i in range(0, 9, 3)]
result = ''
switcher = 1


def output_grid():
    global cells
    print("---------")
    for count in range(3):
        print("|", cells[count][0], cells[count][1], cells[count][2], "|")
    print("---------")


def analyze_grid():
    global cells
    global result
    x_count = o_count = int(0)
    flag_impossible = bool(0)
    for row in cells:
        for cell in row:
            x_count += cell == "X"
            o_count += cell == "O"
    probably_unfinished = [cell == "_" for row in cells for cell in row]
    probably_unfinished = any(probably_unfinished)
    if abs(x_count - o_count) > 1:
        result = "Impossible"
    else:
        for count in range(3):
            if cells[count][0] == cells[count][1] == cells[count][2] != "_":
                if flag_impossible:
                    result = "Impossible"
                    break
                result = str(cells[count][0] + " wins")
                probably_unfinished = 0
                flag_impossible = 1
        for count in range(3):
            if cells[0][count] == cells[1][count] == cells[2][count] != "_":
                if flag_impossible:
                    result = "Impossible"
                    break
                result = str(cells[0][count] + " wins")
                probably_unfinished = 0
                flag_impossible = 1
        if cells[0][0] == cells[1][1] == cells[2][2] != "_":
            result = str(cells[0][0] + " wins")
            probably_unfinished = 0
            if flag_impossible:
                result = "Impossible"
            flag_impossible = 1
        elif cells[0][2] == cells[1][1] == cells[2][0] != "_":
            result = str(cells[0][2] + " wins")
            probably_unfinished = 0
            if flag_impossible:
                result = "Impossible"
        elif not result and probably_unfinished:
            result = ''
        elif not result:
            result = "Draw"
    return result


def take_input():
    global cells
    global switcher
    ok = False
    if switcher == 1:
        cell = "X"
    else:
        cell = "O"
    while not ok:
        coords = input("Enter the coordinates: ").split()
        try:
            coords = [int(coord) - 1 for coord in coords]
        except ValueError:
            print("You should enter numbers!")
            continue
        proper = [0 <= i < 3 for i in coords]
        if not all(proper):
            print("Coordinates should be from 1 to 3!")
        elif cells[coords[0]][coords[1]] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            cells[coords[0]][coords[1]] = cell
            ok = True
    switcher *= -1
    output_grid()


output_grid()

while not result:
    take_input()
    analyze_grid()
print(analyze_grid())
