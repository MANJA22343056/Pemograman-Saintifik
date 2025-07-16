import numpy as np

# 1. persiapan Data
tinggiBadan= np.array([180, 185, 190, 175, 200])
beratBadan = np.array([75, 85, 90, 70, 100])
rataRataPoin = np.array([20, 25, 18, 22, 30])

# 2. analisis Tinggi Badan
# temukan rata-rata tinggi badan pemain
rataRataTinggi = np.mean(tinggiBadan)
print("rata-rata tinggi badan pemain:", rataRataTinggi)

# hitung berapa pemain yang memiliki tinggi badan di atas rata-rata
tinggiDiAtasRataRata = np.sum(tinggiBadan> rataRataTinggi)
print("jumlah pemain dengan tinggi badan di atas rata-rata:", tinggiDiAtasRataRata)

# 3. analisis Berat Badan
# temukan berat badan maksimum dari pemain
beratMaksimum = np.max(beratBadan)
print("berat badan maksimum dari pemain:", beratMaksimum)

# hitung berapa pemain yang memiliki berat badan di bawah rata-rata
rataRataBerat = np.mean(beratBadan)
beratDiBawahRataRata = np.sum(beratBadan < rataRataBerat)
print("jumlah pemain dengan berat badan di bawah rata-rata:", beratDiBawahRataRata)

# 4. analisis Rata-rata Poin
# temukan rata-rata rata-rata poin per game pemain
rataRataPoinPerGame= np.mean(rataRataPoin)
print("rata-rata poin per game pemain:", rataRataPoinPerGame)

# hitung berapa pemain yang mencetak poin di atas rata-rata
poinDiAtasRataRata= np.sum(rataRataPoin > rataRataPoinPerGame)
print("jumlah pemain yang mencetak poin di atas rata-rata:", poinDiAtasRataRata)