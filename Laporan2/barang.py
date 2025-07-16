totalHargaBarang = 0.0
kdBarang = input("Kode barang = ")
namaBarang = input("Nama barang = ")
hargaSatuan = eval(input("Harga satuan barang = Rp. ") )
jumlahBarang = eval (input("Jumlah barang yang dibeli = "))
hargaBeli = hargaSatuan * jumlahBarang
totalHargaBarang = hargaBeli + totalHargaBarang
print("Total harga yang dibayar Rp. ", totalHargaBarang)