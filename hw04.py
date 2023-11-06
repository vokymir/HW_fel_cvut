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

    for i in Symbols:
        print(i.symbol, end=" ")
        print(i.count)

histogram("abcdabcaba")
