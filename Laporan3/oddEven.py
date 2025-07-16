# fungsi isOdd untuk memeriksa apakah bilangan ganjil
def isOdd(number):
    # memeriksa apakah number adalah bilangan bulat dan ganjil
    return isinstance(number, int) and number % 2 != 0


# fungsi isEven untuk memeriksa apakah bilangan genap
def isEven(number):
    # memeriksa apakah number adalah bilangan bulat dan genap
    return isinstance(number, int) and number % 2 == 0


# tes fungsi-fungsi tersebut
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False