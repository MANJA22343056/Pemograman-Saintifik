import pandas as pd

# Nama file CSV yang akan dimodifikasi
file_path = "data16.csv"

# Membaca data dari file CSV ke DataFrame
df = pd.read_csv(file_path)

# Mengubah nilai kolom 'Usia' berdasarkan kondisi tertentu
df.loc[df["Nama"] == "John", "Usia"] = 26

# Menyimpan DataFrame yang telah dimodifikasi kembali ke file CSV
df.to_csv(file_path, index=False)