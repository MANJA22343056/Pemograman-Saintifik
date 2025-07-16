print("========================================================================")
print("         Program Perhitungan Waktu Tempuh dan Biaya Perjalanan          ")
print("========================================================================")
print("                 Programmer: Manja Fani Oktavia                          ")
print("                            Nim: 22343056                                ")
print("                           Studi Kasus No.2                             ")
print("========================================================================\n")

# inisialisasi variabel
hargaPertalite = 9000 # harga pertalite per liter (IDR)
hargaPertamax = 10000 # harga pertamax per liter (IDR)

# input data perjalanan
jenisBahanBakar = input("Masukkan jenis bahan bakar (Pertalite/Pertamax): ").lower()
jarakPerjalanan = float(input("Masukkan jarak perjalanan (km): "))
kecepatanRataRata = float(input("Masukkan kecepatan rata-rata (km/jam): "))
efisiensiBahanBakar = float(input("Masukkan efisiensi bahan bakar kendaraan (km/liter): "))

# hitung waktu tempuh
waktuTempuh = jarakPerjalanan / kecepatanRataRata

# hitung konsumsi bahan bakar
konsumsiBahanBakar = jarakPerjalanan / efisiensiBahanBakar

# hitung biaya perjalanan
if jenisBahanBakar == "pertalite":
    hargaBahanBakar = hargaPertalite
elif jenisBahanBakar == "pertamax":
    hargaBahanBakar = hargaPertamax
else:
    print("Jenis bahan bakar tidak valid.")
    exit()

biayaPerjalanan = konsumsiBahanBakar * hargaBahanBakar

# output
print("------------------------------------------------------------------------")
print("==========================Informasi Perjalanan==========================")
print("------------------------------------------------------------------------")
print(f"Waktu Tempuh: {waktuTempuh:.2f} jam")
print(f"Konsumsi Bahan Bakar: {konsumsiBahanBakar:.2f} liter")
print(f"Total Biaya Perjalanan: IDR {biayaPerjalanan:.2f}")
print("------------------------------------------------------------------------\n")