import math

def hitungRata(angka):
    return sum(angka) / len(angka)

def hitungVariansidanStandarDevisiasi(angka):
    rata = hitungRata(angka)
    variansi = sum((x - rata) ** 2 for x in angka) / len(angka)
    standarDevisiasi = math.sqrt(variansi)
    return variansi, standarDevisiasi

variansi, std_dev = hitungVariansidanStandarDevisiasi([1, 2, 3, 4, 5])
print("Varians dari [1, 2, 3, 4, 5] adalah:", variansi)
print("Deviasi standar dari [1, 2, 3, 4, 5] adalah:", std_dev)