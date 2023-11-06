"""
#dumbest solution
for i in range(100):
    if i%15 == 0:
        print("fizzvizz")
    elif i%5 == 0:
        print("vizz")
    elif i%3 == 0:
        print("fizz")
    else:
        print(i)
"""

"""
#tier 2
for i in range(100):
    out:str = ""
    if i%3 == 0:
        out = out + "fizz"
    if i%5 == 0:
        out = out + "vizz"
    if out == "":
        out = str(i)
    print(out)
"""

"""
#smartest solution I could came up with
for i in range(100):
    print((i%3 == 0)*"fizz" + (i%5 == 0)*"vizz" + (i%3 != 0 and i%5 != 0)*str(i))
"""


#officialy smartest solution
for i in range(100):
    print((i%3 == 0)*"fizz" + (i%5 == 0)*"vizz" or i)
