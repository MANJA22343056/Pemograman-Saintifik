dataDiri = ("Manja Fani Oktavia", "22343056", "Suliki, Payakumbuh")

# ekstrasi elemen-elemen dari tuple
nama, nim, alamat = dataDiri

# print data diri
print(f"Data: {dataDiri}")
print(f"NIM : {nim}")
print(f"NAMA : {nama}")
print(f"ALAMAT : {alamat}")

# konversi NIM ke tuple karakter
nimTuple = tuple(nim)
print(f"NIM: {nimTuple}")

# konversi nama depan ke tuple karakter
namaDepan= nama.split()[0]
namaDepanTuple = tuple(namaDepan)
print(f"NAMA DEPAN: {namaDepanTuple}")

# konversi nama terbalik ke tuple
namaTerbalik = tuple(nama.split()[::-1])
print(f"NAMA TERBALIK: {namaTerbalik}")