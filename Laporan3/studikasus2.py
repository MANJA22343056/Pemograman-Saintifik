print("=============================")
print("======Manja Fani Oktavia=====")
print("===========22343056==========")
print("=============================")
print("Program Menghitung Luas Trapesium")

try:
    alasAtas = float(input("Masukkan panjang alas atas: "))
    alasBawah = float(input("Masukkan panjang alas bawah: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    
    if alasAtas<= 0 or alasBawah <= 0 or tinggi <=0:
        raise ValueError("panjang alasa atau tinggi tidak boleh negatif atau nol.")
    
    luas = 0.5 * (alasAtas + alasBawah) * tinggi
    print("Luas trapesium adalah: ", luas)
except ValueError as salah:
    print("Error:", salah)
except Exception as salah:
    print("Terjadi kesalahan:", salah)