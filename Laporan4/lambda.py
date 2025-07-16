def tambah (a,b):
    hasil = a + b
    return hasil

print("Hasil tambah tanpa menggunakan lambda:")
print(tambah(10,20))

print("Hasil tambah menggunakan lambda:")
tambah = lambda a, b: a + b

print(tambah(10,20))
