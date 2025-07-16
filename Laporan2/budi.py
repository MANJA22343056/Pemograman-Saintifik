# latihan 3

# input gaji /jam dan jumlah jam kerja /minggu
gajiPerJam = float(input("Masukkan gaji per jam:"))
jamKerjaPerMinggu = int(input("Masukkan jumlah jam kerja per minggu: "))

# hitung pendapatan bruto budi selama liburan
pendapatanBruto = gajiPerJam * jamKerjaPerMinggu * 5 # libur 5 minggu

# hitung pendapatan netto setelah potong pajak
pendapatanNetto = pendapatanBruto * (1 - 0.14)

# hitung jumlah uang yang dihabiskan untuk membeli pakaian dan aksesoris
belanjaPakaianAksesoris = pendapatanNetto * 0.01

# hitung jumlah uang yang dihabiskan untuk membeli alat tulis
belanjaAlatTulis = pendapatanNetto * 0.25

# hitung jumlah uang yang akan disedahkan
uangDisedekahkan = pendapatanNetto * 0.25

# hitung jumlah uang yang akan diterima anak yatim
uangAnakYatim = uangDisedekahkan * 0.30

# hitung jumlah uang yang akan diterima kaum dhuafa
uangDhuafa = uangDisedekahkan - uangAnakYatim

# cetak hasil
print("====================================================================================================")
print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak:",pendapatanBruto)
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak:",pendapatanNetto)
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris:",belanjaPakaianAksesoris)
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis:", belanjaAlatTulis)
print("Jumlah uang yang akan Budi sedekahkan:", uangDisedekahkan)
print("Jumlah uang yang akan diterima anak yatim:", uangAnakYatim)
print("Jumlah uang yang akan diterima kaum dhuafa:", uangDhuafa)
print("====================================================================================================")
