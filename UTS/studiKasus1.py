print("========================================================================")
print("   Program Sistem Penilaian Mahasiswa dengan Kategori dan Rekomendasi   ")
print("========================================================================")
print("                 Programmer: Manja Fani Oktavia                          ")
print("                            Nim: 22343056                                ")
print("                           Studi Kasus No.1                             ")
print("========================================================================\n")

# fungsi untuk menghitung nilai akhir mahasiswa
def hitungNilaiAkhir(nilaiTugas, kehadiran, uts, uas):
    bobotTugas = 0.3
    bobotKehadiran = 0.1
    bobotUts = 0.25
    bobotUas = 0.35

    # hitung nilai akhir
    nilaiAkhir = (nilaiTugas * bobotTugas) + (kehadiran * bobotKehadiran) + (uts * bobotUts) + (uas * bobotUas)
    return nilaiAkhir

# fungsi untuk mengonversi nilai akhir menjadi nilai huruf dan memberikan kategori mutu sesuai dengan rentang nilai tertentu.
def konversiNilaiHuruf(nilaiAkhir):
    if 85 <= nilaiAkhir <= 100:
        return "A", "Dengan pujian"
    elif 80 <= nilaiAkhir < 85:
        return "A-", "Sangat baik sekali"
    elif 75 <= nilaiAkhir < 80:
        return "B+", "Baik sekali"
    elif 70 <= nilaiAkhir < 75:
        return "B", "Baik"
    elif 65 <= nilaiAkhir < 70:
        return "B-", "Cukup baik"
    elif 60 <= nilaiAkhir < 65:
        return "C+", "Lebih dari cukup"
    elif 55 <= nilaiAkhir < 60:
        return "C", "Cukup"
    elif 50 <= nilaiAkhir < 55:
        return "C-", "Kurang cukup"
    elif 40 <= nilaiAkhir < 50:
        return "D", "Kurang"
    else:
        return "E", "Gagal"

# fungsi untuk memberikan rekomendasi berdasarkan nilai akhir yang didapat mahasiswa.
def beriRekomendasii(nilaiAkhir):
    if 80 <= nilaiAkhir <= 100:
        return "Anda telah mencapai nilai sangat baik. Pertahankan prestasi Anda!"
    elif 60 <= nilaiAkhir < 80:
        return "Anda memiliki hasil yang cukup baik. Tetap semangat untuk meningkatkan performa Anda!"
    else:
        return "Anda perlu lebih banyak usaha. Evaluasi kembali cara belajar dan persiapkan diri dengan lebih baik."
    
# fungsi 'main' dipanggil untuk menjalankan program utama
def main():
    while True:
        print("------------------------------------------------------------------------")
        print("====================== Sistem Penilaian Mahasiswa ======================")
        print("------------------------------------------------------------------------")
        namaMahasiswa = input("Masukkan nama mahasiswa: ")
        prodi = input("Masukkan program studi: ")
        nilaiTugas = float(input("Masukkan nilai tugas: "))
        kehadiran = float(input("Masukkan persentase kehadiran (dalam persen): "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        print("========================================================================\n")

        nilaiAkhir = hitungNilaiAkhir(nilaiTugas, kehadiran, uts, uas)
        nilaiHuruf, kategoriMutu = konversiNilaiHuruf(nilaiAkhir)

        print("------------------------------------------------------------------------")
        print("============================ Hasil Penilaian =========================")
        print("------------------------------------------------------------------------")
        print("Nama Mahasiswa:", namaMahasiswa)
        print("Program Studi:", prodi)
        print("Nilai Akhir:", nilaiAkhir)
        print("Nilai Huruf:", nilaiHuruf)
        print("Kategori Mutu:", kategoriMutu)
        print("========================================================================\n")

        rekomendasi = beriRekomendasii(nilaiAkhir)
        print("\n📍 Rekomendasi:", rekomendasi)

        lanjut = input("\nApakah Anda ingin melanjutkan? (ya/tidak): \n")
        if lanjut.lower() != "ya":
            print("\n💡 Selamat! Anda telah selesai menggunakan program sistem penilaian.")
            break

main()