# nilai kurs 1 US$ ke IDR
kursUSD = 13950

# informasi program
print('Program konversi US$ ke IDR')
print('Kurs saat ini 1 US$ =', kursUSD, 'Rupiah')

# input jumlah US$ yang mau ditukar
jumlahUSD = float(input('Masukkan jumah uang yang mau ditukar ke Rupiah: '))

# hitung nilainya dalam Rupiah
dalamRupiah = jumlahUSD * kursUSD

# tampilkan hasilnya
print('Hasil konversi = Rp. ', dalamRupiah) 
