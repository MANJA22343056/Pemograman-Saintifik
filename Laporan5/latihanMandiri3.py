# input jumlah mata kuliah
jumlahMatkul = int(input("Berapa jumlah mata kuliah? "))

# input nilai setiap mata kuliah
nilaiMatkul = []
for i in range(jumlahMatkul):
    nilai = input("Nilai MK {}: ".format(i + 1))
    nilaiMatkul.append(nilai)

# hitung total bobot nilai
totalBobotNilai = 0
for nilai in nilaiMatkul:
    if nilai == "A":
        bobotNilai = 4
    elif nilai == "B":
        bobotNilai = 3
    elif nilai == "C":
        bobotNilai = 2
    elif nilai == "D":
        bobotNilai = 1
    else:
        bobotNilai = 0

    totalBobotNilai += bobotNilai

# Menghitung nilai IPS
ips = totalBobotNilai / jumlahMatkul

# tampilkan hasil IPS
print("Nilai IPS Anda semester ini:", ips)