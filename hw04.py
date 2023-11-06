# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw04

class Symbol:
    """
    Object for symbols in given text, and number of it's occurrence
    """
    def __init__(self, symbol:str, count:int=1):
        self.symbol = symbol
        self.count = count

def histogram(text:str, scale:int=1, case_sensitive:bool=False):
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


















#tests from assignment
"""
histogram('Ahoj svete, kde to kvete', 0)
histogram('Ahoj svete, kde to kvete', 10)
histogram('Aaaach, to je kraaasa', 4)
"""