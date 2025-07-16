import math

def prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(math.sqrt(angka)) + 1):
        if angka % i == 0:
            return False
    return True

print("Apakah 7 adalah bilangan prima?", prima(7))