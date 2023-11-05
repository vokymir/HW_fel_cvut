# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw03

class Guess:
    def __init__(self, shiftBy:int, shiftedTo:str, similarTo:int):
        self.shiftBy = shiftBy
        self.shiftedTo = shiftedTo
        self.similarTo = similarTo


def dekoduj(sifrovany:str, odposlechnuty:str):
    #abc:list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    abc:str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(sifrovany)):
        x = sifrovany[i]
        if(x>"z" or x<"A" or (x>"Z" and x<"a")):
            print("Error: Chybny vstup!")
            return None
    for i in range(len(odposlechnuty)):
        x = odposlechnuty[i]
        if(x>"z" or x<"A" or (x>"Z" and x<"a")):
            print("Error: Chybny vstup!")
            return None
    if(len(sifrovany) != len(odposlechnuty)):
        print("Error: Chybna delka vstupu!")
        return None
    resemblence:list[Guess] = []
    for i in range(len(abc)):
        shifted:str = ""
        similarity:int = 0
        for j in range(len(sifrovany)):
            y:int = (int(abc.index(sifrovany[j]))+i)%len(abc)
            shifted = shifted + abc[y]
            if(shifted[j]==odposlechnuty[j]):
                similarity += 1
        resemblence.append(Guess(i,shifted,similarity))
    res:str = sifrovany
    howmuch:int = 0
    for i in range(len(resemblence)):
        if(resemblence[i].similarTo > howmuch):
            res = resemblence[i].shiftedTo

    return res


print(dekoduj("xUbbemehbT","XYlloworld"))