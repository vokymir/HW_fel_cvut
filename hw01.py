# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw01

def triangle(inc:bool, width:int, rows:int, gap:int):
    start:int
    end:int
    step:int
    if(inc == True):
        start = width - 2 * rows + 2
        end = width + 1
        step = 2
    else:
        start = width
        end = width - 2 * rows + 2 - 1
        step = -2
    for i in range(start, end, step):
        for j in range(gap):
            print(" ", end="")
        for j in range(int((width-i)/2)):
            print(" ", end="")
        for j in range(i):
            print("x", end="")
        print("")

def sand_hours(width:int):
    if(width % 2 == 0):
        raise Exception("sand_hours only except odd numbers")
    print("$", end="")
    for i in range(width-2):
        print("-", end="")
    print("$")
    triangle(False, width-2, int((width-2 + 1) / 2), 1)
    triangle(True,  width-2, int((width-2 + 1) / 2)-1, 1)
    print("$", end="")
    for i in range(width-2):
        print("-", end="")
    print("$")




sand_hours(11)