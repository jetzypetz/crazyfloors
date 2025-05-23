import random
from PIL import Image
list1 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'f']
x, last_outcome, penultimate = [0, 0, 0]
floor = []
end = False
s0 = []
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []
s10 = []
s11 = []
for i in [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]:
    for j in range(18):
        i.append([])
        for k in range(18):
            i[j].append(1)
shapes = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
for i in range(18):
    for j in [s0, s2, s4, s6, s7, s10, s11]:
        j[i][0] = 0
    for j in [s1, s3, s4, s5, s6, s10, s11]:
        j[i][17] = 0
    for j in [s0, s1, s4, s5, s7, s8, s9]:
        j[0][i] = 0
    for j in [s2, s3, s5, s6, s7, s8, s9]:
        j[17][i] = 0
    for j in [s0, s3, s9, s11]:
        j[i][i] = 0
        j[i][i - 1] = 0
        j[i - 1][i] = 0
    for j in [s1, s2, s8, s10]:
        j[i][-i] = 0
        j[i][-i - 1] = 0
        j[i - 1][-i - 1] = 0


def create_rect_floor(length, width):  # make_letter
    global floor
    floor = []
    for k in range(length):
        floor.append([])
        for y in range(width):
            floor[k].append(None)
    for flip in range(3):
        for flop in range(12):
            floor[-flip - 1][flop] = False
        for flop in range(25, 31):
            floor[-flip - 1][flop] = False
    for o in range(length * width * 2):
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
                floor[q + 1][r + 1] = 'a3'
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
                    floor[q + 1][r + 1] = 'a2'
                else:
                    not_placed += 1
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'd':
        try:
            if floor[q + 1][r - 1] is None and r > 0:
                floor[q][r] = 'c1'
                floor[q + 1][r - 1] = 'b1'
                floor[q + 1][r] = 'd3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'e':
        try:
            if floor[q][r + 1] is None and floor[q][r + 2] is None:
                floor[q][r] = 'b1'
                floor[q][r + 1] = 'e2'
                floor[q][r + 2] = 'a2'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1
    elif p == 'f':
        try:
            if floor[q + 1][r] is None and floor[q + 2][r] is None:
                floor[q][r] = 'c1'
                floor[q + 1][r] = 'f2'
                floor[q + 2][r] = 'a3'
            else:
                not_placed += 1
        except IndexError:
            not_placed += 1


while not end:
    create_rect_floor(18, 31)
floor2 = []
for g in range(18 * 18):
    floor2.append([])
    for h in range(31 * 18):
        floor2[g].append(None)
for blip in range(18):
    for blop in range(31):
        rand = random.randint(0, 1)
        for blap in range(18):
            for blup in range(18):
                if floor[blip][blop] == 'a1':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s0[blap][blup]
                elif floor[blip][blop] == 'b2':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s1[blap][blup]
                elif floor[blip][blop] == 'c2':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s2[blap][blup]
                elif floor[blip][blop] == 'd3':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s3[blap][blup]
                elif floor[blip][blop] == 'c1':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s4[blap][blup]
                elif floor[blip][blop] == 'a2':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s5[blap][blup]
                elif floor[blip][blop] == 'a3':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s6[blap][blup]
                elif floor[blip][blop] == 'b1':
                    floor2[blip * 18 + blap][blop * 18 + blup] = s7[blap][blup]
                elif floor[blip][blop] == 'e2':
                    if rand == 1:
                        floor2[blip * 18 + blap][blop * 18 + blup] = s8[blap][blup]
                    else:
                        floor2[blip * 18 + blap][blop * 18 + blup] = s9[blap][blup]
                elif floor[blip][blop] == 'f2':
                    if rand == 1:
                        floor2[blip * 18 + blap][blop * 18 + blup] = s10[blap][blup]
                    else:
                        floor2[blip * 18 + blap][blop * 18 + blup] = s11[blap][blup]
                else:
                    floor2[blip * 18 + blap][blop * 18 + blup] = 1
img = Image.new('1', (324, 558))
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = floor2[i][j]
img.save('whitebig18', 'bmp')
img.show()
