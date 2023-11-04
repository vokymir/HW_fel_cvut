# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw03

def dekoduj(sifrovany:str, odposlechnuty:str):
    abc:list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for x in sifrovany:
        if(x>"Z" or x<"a" or (x>"z" and x<"A")):
            print("Error: Chybny vstup!")
            return None
    for x in odposlechnuty:
        if(x>"Z" or x<"a" or (x>"z" and x<"A")):
            print("Error: Chybny vstup!")
            return None
    if(len(sifrovany) != len(odposlechnuty)):
        print("Error: Chybna delka vstupu!")
        return None
    




    return "ahoj"