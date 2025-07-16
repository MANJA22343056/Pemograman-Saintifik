import math
def kpk(a,b):
    return abs(a*b) // math.gcd(a,b)

print("KPK dari 30 dan 20 adalah:", kpk(30, 20))