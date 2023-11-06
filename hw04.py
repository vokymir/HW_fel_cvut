# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw04

class Symbol:
    def __init__(self, symbol:str, count:int=1):
        self.symbol = symbol
        self.count = count

def histogram(text:str, scale:int=1, case_sensitive:bool=False):
    Symbols:list[Symbol] = []
    for x in text:
        done:bool = False
        for y in Symbols:
            if(x == y.symbol):
                y.count += 1
                done = True
                break
        if (done == False):
                Symbols.append(Symbol(x))

    for i in range(len(Symbols)):
        for j in range(len(Symbols)-i-1):
            if(Symbols[j].symbol > Symbols[j+1].symbol):
                help:Symbol = Symbols[j]
                Symbols[j] = Symbols[j+1]
                Symbols[j+1] = help
    
    SymbolsII:list[tuple] = []
    for k in Symbols:
        print(k.symbol, end=": ")
        print("*"*k.count)
        SymbolsII.append((k.symbol, k.count))
    
    return SymbolsII

print(histogram("wabcdabcdsgjthwoievufnwohnaciugfqoaerucgynqpaoidcfhaewhiofaba"))
