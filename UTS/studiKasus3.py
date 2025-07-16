print("========================================================================")
print("                      Program Pemenang Lomba Lempar Lembing              ")
print("========================================================================")
print("                 Programmer: Manja Fani Oktavia                          ")
print("                            Nim: 22343056                                ")
print("                           Studi Kasus No.3                              ")
print("========================================================================\n")

# fungsi untuk validasi input jarak lemparan
def validasiJarak(jarak):
    if jarak <= 0:
        print("Jarak lemparan harus lebih besar dari 0.")
        return False
    return True

# input jumlah peserta lomba
jumlahPeserta = int(input("Masukkan jumlah peserta lomba: "))

# inisialisasi variabel
namaPemenang = ""
jarakTerjauh = 0

# input data peserta dan penentuan pemenang
for i in range(1, jumlahPeserta + 1):
    print(f"\nData Peserta ke-{i}:")
    namaPeserta = input("Masukkan nama peserta: ")
    jarakLemparan = float(input("Masukkan jarak lemparan (meter): "))

    # validasi input jarak lemparan
    while not validasiJarak(jarakLemparan):
        jarakLemparan = float(input("Masukkan jarak lemparan (meter): "))

    # penentuan pemenang
    if jarakLemparan > jarakTerjauh:
        jarakTerjauh = jarakLemparan
        namaPemenang = namaPeserta

# output pemenang lomba
print("========================================================================")
print("                        ~~~Pemenang Lomba~~~                            ")
print("========================================================================")
print(f"  🏆 Pemenang lomba adalah {namaPemenang} dengan lemparan sejauh {jarakTerjauh} meter. 🏆")
print("========================================================================")