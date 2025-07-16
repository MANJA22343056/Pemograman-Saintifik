n = int(input("masukkan jumlah katagori: "))

dataAplikasi = {}

for i in range(n):
    namaKatagori = input("masukkan nama katagori: ")
    print("masukkan 5 nama aplikasi di katagori ", namaKatagori)
    
    aplikasi = []
    for j in range(5):
        namaAplikasi = input("nama aplikasi: ")
        aplikasi.append(namaAplikasi)
        
        dataAplikasi[namaKatagori] = aplikasi
    
print(dataAplikasi)

daftarAplikasiList = []
for aplikasi in dataAplikasi.values():
    daftarAplikasiList.append(set(aplikasi))
    
print(daftarAplikasiList)

hasil = daftarAplikasiList[0]
for i in range(1, len(daftarAplikasiList)):
    hasil = hasil.intersection(daftarAplikasiList[i])
    
print(hasil)