# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw04

class Symbol:
    """
    Object for symbols in given text, and number of it's occurrence
    """
    def __init__(self, symbol:str, count:int=1):
        self.symbol = symbol
        self.count = count

def histogram(text:str, scale:int=1, case_sensitive:bool=False) -> list:
    Symbols:list[Symbol] = []
    biggest:int = 0
    # if it's not case sensitive, it switches everything to lowercase
    if not(case_sensitive):
        text = text.casefold()
    """
    Iterates the whole text string, and for each valid char checks if the Symbol object already exist,
    if so, it adds 1, otherwise create new. Simultanuously we look for the char with the highest occurance.
    """
    for x in text:
        if (not(x<"A" or x>"z" or (x>"Z" and x <"a"))):
            done:bool = False
            for y in Symbols:
                if(x == y.symbol):
                    y.count += 1
                    if y.count > biggest:
                        biggest = y.count
                    done = True
                    break
            if (done == False):
                    Symbols.append(Symbol(x))

    # scales the number of *
    modifier:float = 1
    if scale != 0:
        modifier = scale / biggest

    # order the Symbols list by the alphabet
    for i in range(len(Symbols)):
        for j in range(len(Symbols)-i-1):
            if(Symbols[j].symbol > Symbols[j+1].symbol):
                help:Symbol = Symbols[j]
                Symbols[j] = Symbols[j+1]
                Symbols[j+1] = help
    # create another list for return reasons, and print the histogram
    SymbolsII:list[tuple] = []
    for k in Symbols:
        print(k.symbol, end=": ")
        print("*"*int(k.count*modifier))
        SymbolsII.append((k.symbol, k.count))
    
    return SymbolsII

def serad(text:str, metoda:int, case_sensitive:bool = False) -> list:
    res:list[tuple] = []
    Htext:str = ""
    # get rid of non-alphabetical characters
    for i in text:
        if (not(i<"A" or i>"z" or (i>"Z" and i <"a")) or i==" "):
            Htext = Htext + i
    text = Htext

    
    words:list[str] = text.split(" ")
    
    for i in words:
        #get rid of short words
        if len(i)<4:
            words.remove(i)
        else:
            # compare by word length
            if metoda == 0:
                res.append((i, len(i)))
            # compare by consonant (not-vowel) -> subtract count of vowel
            elif metoda == 1:
                res.append((i, len(i) - i.count("a") - i.count("A") - i.count("e") -i.count( "E") -i.count( "i") -i.count( "I") - i.count( "y") -i.count("Y") -i.count("o")-i.count( "O") -i.count("u") -i.count("U")))
            # compare by most-used char
            elif metoda == 2:
                Symbols:list[Symbol] = []
                biggest:int = 0
                # for every letter in each word
                for pismeno in i:
                    done:bool = False
                    # case sensitivness done
                    if case_sensitive:
                        pismenko = pismeno
                    else:
                        pismenko = pismeno.casefold()
                    # check, if already counting, if so add 1, otherwise start counting
                    for znak in Symbols:
                        if(pismenko == znak.symbol):
                            znak.count += 1
                            if znak.count > biggest:
                                biggest = znak.count
                            done = True
                            break
                    if (done == False):
                        Symbols.append(Symbol(pismenko))
                # append word with how many times the most used char was used
                res.append((i, biggest))
    # sort by numeric value (dependant on method)
    for j in range(len(res)):
        for k in range(len(res)-j-1):
            if res[k][1] < res[k+1][1]:
                help:tuple = res[k]
                res[k] = res[k+1]
                res[k+1] = help
    # sort by alphabet
    for j in range(len(res)):
        for k in range(len(res)-j-1):
            if res[k][1] == res[k+1][1] and res[k][0] > res[k+1][0]:
                help = res[k]
                res[k] = res[k+1]
                res[k+1] = help        
    # copy res to resres in desired output
    resres:list[str] = []
    for l in range(len(res)):
        resres.append(res[l][0])

    return resres

#tests from assignment
"""
histogram('Ahoj svete, kde to kvete', 0)
histogram('Ahoj svete, kde to kvete', 10)
histogram('Aaaach, to je kraaasa', 4)
"""

"""
print(serad('Aaaach, to je kraaasa', 0, True))
print(serad('Aaaach, to je kraaasa', 2, True))
print(serad('Aaaach, to je kraaasa', 2, False))
"""