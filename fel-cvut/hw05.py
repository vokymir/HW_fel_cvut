# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw05

def validate(x:tuple,name:str,minus:int) -> tuple:
    if(x[0] == False):
        return (False, None, [])
    else:
        modified:str = name[:(len(name)-minus)]
        shouldAppend:bool = True
        for xmlSign in x[2]:
            if xmlSign == modified:
                shouldAppend = False
        if shouldAppend:
            x[2].append(modified)
        return (True, x[1] + 1, x[2])

def xml(text:str) -> tuple:
    txtL = text.partition("<")
    txtR = txtL[2].partition(">")
    if "/" in txtR[0]:
        x = xml(txtR[2])
        return validate(x,txtR[0],1)
    spoj:str = "</" + txtR[0] + ">"
    txtM = txtR[2].partition(spoj)
    if "<" in txtM[0]:
        x = xml(txtM[0])
        return validate(x,txtR[0],0)
        # if(x[0] == False):
        #     return (False, None, [])
        # else:
        #     x[2].append(txtR[0])
        #     return (True, x[1] + 1, x[2])
    if "<" in txtM[2]:
        x = xml(txtM[2])
        return validate(x, txtR[0], 0)
        # if(x[0] == False):
        #     return (False, None, [])
        # else:
        #     x[2].append(txtR[0])
        #     return (True, x[1] + 1, x[2])
    if txtM[1] == "" and txtL[1] != "":
        return (False, None, [])
    if txtM[1] == "" and txtL[1] == "":
        return (True, 0, [])
    return (True, 1, [txtR[0]])

print(xml("<a><c/></a><b/>"))
#print(xml("<a><b></a></b>"))
#print(xml('<a><b>10</b><c>ahoj svete</c><d/><d/></a>'))
#print(xml('<table><tr><td>10</td><td>20</td></tr><tr><td><img/></td></tr></table>'))