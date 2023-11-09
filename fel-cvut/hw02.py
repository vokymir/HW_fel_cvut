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

    Args:
        arr1: Prime defactorization of first number.
        arr2: Prime defactorization of second number.
    
    Returns:
        INT number, the smallest divider of the two numbers given in arrays.
    """
    arr1_copy:list[int] = arr1.copy()
    arr2_copy:list[int] = arr2.copy()
    res:int = 1
    while len(arr2_copy) > 0:
        for i in range(len(arr1_copy)):
            if(arr2_copy[0]==arr1_copy[i]):
                res *= arr1_copy[i]
                del arr1_copy[i]
                break
        del arr2_copy[0]
                
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
            
            if(j==k-1):
                print("")
            else:
                print("|", end="")
            arr_j.clear()
        arr_i.clear()
        print("-"*(k*2-1))

tabulka(10)