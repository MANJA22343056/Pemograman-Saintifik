# mendefinisikan lamda untuk menghitung biaya total pembelian rumah
hitungBiayaTotal = lambda hargaRumah, pajak, biayaAdmin: hargaRumah + (hargaRumah * pajak) + biayaAdmin

hargaRumah = 20000000
pajak = 0.1
biayaAdmin = 3000000
biayaTotal = hitungBiayaTotal (hargaRumah, pajak, biayaAdmin)

print("Biaya total beli rumah: ", biayaTotal)