def pemangkatanTanpaOperator(a, b):
    hasil = 1
    for _ in range(b):
        hasil *= a
    return hasil

bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
hasilPemangkatan = pemangkatanTanpaOperator(bilangan1, bilangan2)
print("Hasil pemangkatan:", hasilPemangkatan)