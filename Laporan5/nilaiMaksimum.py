def temukanMaksimum(angka):
    nilaiMaksimum = angka[0]
    for num in angka:
        if num > nilaiMaksimum:
            nilaiMaksimum = num
    return nilaiMaksimum

print("Nilai maksimum dari [5, 3, 8, 1, 9] adalah:", temukanMaksimum([5, 3, 8, 1, 9]))