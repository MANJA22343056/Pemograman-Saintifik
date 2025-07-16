def temukanMinimum(angka):
    nilaiMinimum = float('inf')
    for num in angka:
        if num < nilaiMinimum:
            nilaiMinimum = num
    return nilaiMinimum

print("Nilai minimum dari [5, 3, 8, 1, 9] adalah:", temukanMinimum([5, 3, 8, 1, 9]))