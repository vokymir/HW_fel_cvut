# https://cw.fel.cvut.cz/wiki/courses/bab37zpr/hw/hw02

def divided_by(num:int,arr:list[int]):
    """
    Fill the given array with prime numbers to which the given number could be divided.

    Args:
        num: Any number from 1 above.
        arr: List to which the prime numbers would append.
    """
    x:int = 2
    while (num>1):
        if(num%x==0):
            arr.append(x)
            num = int(num/x)
        else:
            x += 1

def small_div(arr1:list[int], arr2:list[int]) -> int:
    """
    Finds a smallest divider of two numbers given as prime defactorization in arrays arr1 and arr2, and returns it.
    !!!This function will cannibalize the arr2!!!

    Args:
        arr1: Prime defactorization of first number.
        arr2: Prime defactorization of second number.
    
    Returns:
        INT number, the smallest divider of the two numbers given in arrays.
    """
    res:int = 1
    for i in range(len(arr1)-1):
        for j in range(len(arr2)-1):
            if(arr1[i]==arr2[j]):
                res += arr1[i]
                del arr2[j]
                break
    return res

def tabulka(k:int):
    if(k<1 or k>99):
        print("ERROR")
        return
    for i in range(k):
        arr_i:list[int] = [1]
        divided_by(i+1,arr_i)
        for j in range(k):
            arr_j:list[int] = [1]
            divided_by(j+1,arr_j)
            div:int = small_div(arr_i, arr_j)
            if(div>1):
                print("x", end="")
            else:
                print(" ", end="")
            del arr_j
            if(j==k-1):
                print("")
            else:
                print("|", end="")
        del arr_i
        print("-"*(k*2-1))

tabulka(4)