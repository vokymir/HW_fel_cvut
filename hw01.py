# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw01

def triangle(inc:bool, width:int, rows:int, gap:int, symbol:str):
    """
    Will print a triangle, or it's part.

    Args:
        inc: Is increasing. == Is is wider at the bottom?
        width: How width it is at the widest row. Should be an odd number for triangle with only one tip.
        rows: How many rows it shoul print, it prints the widest row every time, and then (rows-1) rows. If entered more than the triangle require, it will leave a blank space.
        gap: How wide should the gap before be? Useful in funkce_1.
        symbol: What symbol are we using to create a triangle? Only use 1 char.
    """
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
            print(symbol, end="")
        print("")

def row(border:str, inside:str, border_width:int, inside_width:int):
    """
    Prints a row with border chars on sides and inside chars in the middle, e.g. #----#.

    Args:
        border: Char (or string) which will be on the sides.
        inside: Char (or string) which will be in the middle.
        border_width: How many border symbols on each side.
        inside_width: How many inside symbols in the middle.
    """
    for i in range(border_width):
        print(border, end="")
    for i in range(inside_width):
        print(inside, end="")
    for i in range(border_width):
        print(border, end="")
    print("")

def funkce_1(width:int) -> int:
    if(width % 2 == 0):
        raise Exception("funkce_1 only except odd numbers")
    if(width < 3 or width >= 20):
        return 1
    row("$","-",1,width-2)
    triangle(False, width-2, int((width-2 + 1) / 2), 1, "x")
    triangle(True,  width-2, int((width-2 + 1) / 2)-1, 1, "x")
    row("$","-",1,width-2)
    return 0

def funkce_2(width:int, height:int):
    if(width % 2 == 0):
        raise Exception("funkce_2 only except odd numbers")
    if(width < 3 or width >= 20):
        return 1
    if(height >= width):
        return 2
    print(" "* int(width/2)+"o")
    triangle(True,width,int(width/2),0,"@")
    for i in range(height):
        row("@","x",1,width-2)
    triangle(False,width,int(width/2),0,"@")
    print(" "* int(width/2)+"o")
    return 0

def funkce_3(width:int, height:int, char:str):
    if(width % 2 == 0):
        raise Exception("funkce_2 only except odd numbers")
    if(width < 3 or width >= 20):
        return 1
    if(height >= width):
        return 2
    if(char < "a" or char > "z"):
        return 3
    triangle(True,width,int((width+1)/2),0,"^")
    for i in range(height):
        row("|", char, 1, width-2)
    return 0