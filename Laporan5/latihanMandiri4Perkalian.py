def perkalianTanpaOperator(a, b):
    hasil = 0
    for _ in range(abs(b)):
        hasil += a
    if b < 0:
        hasil = -hasil
    return hasil

bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
hasilPerkalian = perkalianTanpaOperator(bilangan1, bilangan2)
print("Hasil perkalian:", hasilPerkalian)