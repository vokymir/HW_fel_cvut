# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw05
# just 1 issue: the outputed list at tuple[3] is in wrong order, compared to the assignment

def validate(x:tuple,name:str,minus:int, numOfSign:int) -> tuple:
    """
    Validate, if the tuple isn't redundant (False),
    finds if the name of XML Sign ends with / and removes it,
    doesn't include duplicates in list of XML Signs.
    Args:
        x: The tuple you want to validate, should be given as (bool, int, list[string]).
        name: Name of the XML Sign (e.g. from <p></p> is "p")
        minus: If you want to slice the name from the end (e.g. 1: "img/" -> "img")
        numOfSign: Number of XML Signs in the string.
    Returns:
        Tuple, but validated.
    """
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
        return (True, numOfSign, x[2])
    


def xml(text:str) -> tuple:
    """
    Recursive function, it slices the string into parts and looks for valid XML Signs in each.
    The numOfSign is only needed once, but because I started with recursive function, it's in each run...
    Args:
        text: XML text to validate.
    Returns:
        Tuple containing (bool, int, list[str]), where bool tells if the text is valid XML. 
        Int is for how many times valid XML tags (signs) occured in it. 
        List contains the valid tags.

    Imagine a text, and behold which part is which in terms of txt L,R,M:
            <a><b></a></b>
    txtL:--012222222222222
    txtR:----0122222222222
    txtM:------00011112222
    """
    numOfSign:int = text.count("</")+text.count("/>")
    txtL = text.partition("<")
    txtR = txtL[2].partition(">")
    if "/" in txtR[0]:
        x = xml(txtR[2])
        return validate(x,txtR[0],1,numOfSign)
    spoj:str = "</" + txtR[0] + ">"
    txtM = txtR[2].partition(spoj)
    if "<" in txtM[0] or "<" in txtM[2]:
        x = validate(xml(txtM[0]), txtR[0], 0, numOfSign)
        y = validate(xml(txtM[2]), txtR[0], 0, numOfSign)
        if x[0] == False or y[0] == False:
            return (False, None, [])
        joinList:list = x[2].copy() + y[2].copy()
        for item in joinList:
            if joinList.count(item) > 1:
                joinList.remove(item)
        return (True, numOfSign, joinList)
    if txtM[1] == "" and txtL[1] != "":
        return (False, None, [])
    if txtM[1] == "" and txtL[1] == "":
        return (True, 0, [])
    return (True, 1, [txtR[0]])


print(xml("<a><b></a></b>"))
print(xml('<a><b>10</b><c>ahoj svete</c><d/><d/></a>'))
print(xml('<table><tr><td>10</td><td>20</td></tr><tr><td><img/></td></tr></table>'))