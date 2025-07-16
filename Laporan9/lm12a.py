# definisi aplikasi
aplikasiKategori = {
    "Kategori 1": ["Shopee", "Lazada", "Tokopedia"],
    "Kategori 2": ["Mobile Legend", "Car", "Pong"],
    "Kategori 3": ["Instagram", "WhatsApp", "Telegram"],
}

jumlahKemunculan = {}

for kategori, aplikasiList in aplikasiKategori.items():
    for aplikasi in aplikasiList:
        if aplikasi in jumlahKemunculan:
            jumlahKemunculan[aplikasi] += 1
        else:
            jumlahKemunculan[aplikasi] = 1

# tampilkan aplikasi yang hanya muncul di satu kategori saja
aplikasiSatuKategori = [app for app, count in jumlahKemunculan.items() if count == 1]
print("Aplikasi yang hanya muncul di satu kategori saja:")
print(aplikasiSatuKategori)


# fungsi untuk menampilkan aplikasi yang muncul tepat di dua kategori sekaligus
def aplikasiDuaKategori(jumlahKemunculan):
    aplikasiDua = [app for app, count in jumlahKemunculan.items() if count == 2]
    return aplikasiDua


# input n>2 dan panggil fungsi aplikasiDuaKategori
n = int(input("Masukkan nilai n (n>2): "))

if n > 2:
    aplikasiDua = aplikasiDuaKategori(jumlahKemunculan)
    print("Aplikasi yang muncul tepat di dua kategori sekaligus:")
    print(aplikasiDua)
else:
    print("Nilai n harus lebih besar dari 2")
