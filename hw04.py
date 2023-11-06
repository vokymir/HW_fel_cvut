# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw04

class Symbol:
    def __init__(self, symbol:str, count:int=0) -> None:
        self.symbol = symbol
        self.count = count

def histogram(text:str, scale:int=0, case_sensitive:bool=False):
    Symbols:list[Symbol] = []
    for x in text:
        Symbols.append(Symbol(x))
    for i in Symbols:
        print(i.symbol, end="")
        print(i.count)

histogram("abcdabcaba")