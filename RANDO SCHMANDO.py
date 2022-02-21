import random
list1 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'f']
x, last_outcome, penultimate = [0, 0, 0]
floor = []
end = False


def create_rect_floor(i, j):  # make_letter
    global floor
    floor = []
    for k in range(i):
        floor.append([])
        for y in range(j):
            floor[k].append(None)
    for o in range(i * j * 2):
        make_letter()


def make_letter():  # find_space...
    global x
    global last_outcome
    global penultimate
    x = list1[random.randint(0, len(list1) - 1)]
    if x == last_outcome or x == penultimate:
        make_letter()
    else:
        find_space_to_put_shape(x)
        penultimate = last_outcome
        last_outcome = x


def find_space_to_put_shape(p):  # put_shape()
    global end
    row = 0
    column = 0
    try:
        while floor[row][column] is not None:
            try:
                while floor[row][column] is not None:
                    column += 1
            except IndexError:
                column = 0
                row += 1
    except IndexError:
        end = True
    put_shape(p, row, column)


def put_shape(p, q, r):
    not_placed = 0
    if p == 'a':
        try:
            if floor[q][r + 1] is None and floor[q + 1][r] is None:
                floor[q][r] = 'a1'
                floor[q][r + 1] = 'a2'
                floor[q + 1][r] = 'a3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'b':
        try:
            if floor[q][r + 1] is None and floor[q + 1][r + 1] is None:
                floor[q][r] = 'b1'
                floor[q][r + 1] = 'b2'
                floor[q + 1][r + 1] = 'b3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'c':
        try:
            if floor[q + 1][r] is None and floor[q + 1][r + 1] is None:
                if floor[q][r + 1] == floor[q][r + 2] or (
                        floor[q][r + 1] is not None and floor[q][r + 2] is not None):
                    floor[q][r] = 'c1'
                    floor[q + 1][r] = 'c2'
                    floor[q + 1][r + 1] = 'c3'
                else:
                    not_placed += 1
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'd':
        try:
            if floor[q + 1][r - 1] is None and r > 0:
                floor[q][r] = 'd1'
                floor[q + 1][r - 1] = 'd2'
                floor[q + 1][r] = 'd3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'e':
        try:
            if floor[q][r + 1] is None and floor[q][r + 2] is None:
                floor[q][r] = 'e1'
                floor[q][r + 1] = 'e2'
                floor[q][r + 2] = 'e3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'f':
        try:
            if floor[q + 1][r] is None and floor[q + 2][r] is None:
                floor[q][r] = 'f1'
                floor[q + 1][r] = 'f2'
                floor[q + 2][r] = 'f3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1


checker = 0
while checker != 36:
    create_rect_floor(15, 31)
    checker = 0
    for check1 in range(13, 15):
        for check2 in range(12):
            if floor[check1][check2] is not None:
                checker += 1
        for check3 in range(25, 31):
            if floor[check1][check3] is not None:
                checker += 1
print(floor)
