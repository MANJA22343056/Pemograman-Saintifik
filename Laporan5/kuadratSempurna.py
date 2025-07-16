import math 
def kuadratSempurna(angka):
    akar = math.isqrt(angka)
    return akar * akar == angka

print("Apakah 16 adalah bilangan kuadrat sempurna?", kuadratSempurna(16))