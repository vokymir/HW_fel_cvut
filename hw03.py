# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw03

class Guess:
    def __init__(self, shiftBy:int, shiftedTo:str, similarTo:int):
        self.shiftBy = shiftBy
        self.shiftedTo = shiftedTo
        self.similarTo = similarTo


def dekoduj(sifrovany:str, odposlechnuty:str):
    #abc:list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    abc:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    """
    Checking if input is valid.
    """
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
    """
    for every possible shift of letters
        for every letter in word
            finds a shifted letter, and if it equals letter from almost-decrypted text, ++
        save the guess of the word
        if it's more accurate than the yet most accurate, swap
    """
    resemblence:list[Guess] = []
    res:str = sifrovany
    howmuch:int = 0
    for i in range(len(abc)):
        shifted:str = ""
        similarity:int = 0
        for j in range(len(sifrovany)):
            y:int = (int(abc.index(sifrovany[j]))+i)%len(abc)
            shifted = shifted + abc[y]
            if(shifted[j]==odposlechnuty[j]):
                similarity += 1
        resemblence.append(Guess(i,shifted,similarity))
        k:Guess = resemblence[i]
        if(k.similarTo > howmuch):
            res = k.shiftedTo
            howmuch = k.similarTo    
    #end of procedure, returns a most similar to almost-decrypted result
    return res




print(dekoduj("xUbbemehbT","XYlloworld"))
print(dekoduj("mnoXYhnTLJ","JCudvgtXRi"))
print(dekoduj("fghQRa-CEC","scbdeMKARZ"))
print(dekoduj("fghQRa","scbdeMK"))
print(dekoduj("IbxlNFcbyWfbhYrtraqlPrfxrubVagreargh", "VukyAfpTlJsoJLeeeeeeCeksehoIttertetu"))