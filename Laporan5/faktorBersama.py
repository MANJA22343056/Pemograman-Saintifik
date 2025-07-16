import math

def temukanFaktorBersama(angka):
    faktorBersama = angka[0]
    for num in angka[1:]:
        faktorBersama = math.gcd(faktorBersama, num)

print("Faktor bersama dari [12, 18, 24] adalah:", temukanFaktorBersama([12, 18, 24]))