# mendefinisikan fungsi untuk memesan tiket bioskop
def pesanTiketBioskop (namaFilm, jumlahTiket, hargaTiket):
    totalBiaya = jumlahTiket * hargaTiket
    print("===Pemesanan Tiket===")
    print("Film: ", namaFilm)
    print("Jumlah Tiket: ", jumlahTiket)
    print("Harga Tiket: ", hargaTiket)
    print("Total Biaya: ", totalBiaya)
    return totalBiaya

# panggil fungsi
namaFilm = " Fast Furious"
jumlahTiket = 2
hargaTiket = 35000
totalBiaya = pesanTiketBioskop(namaFilm, jumlahTiket, hargaTiket)
print("Lakukan pembayaran Rp.", totalBiaya)