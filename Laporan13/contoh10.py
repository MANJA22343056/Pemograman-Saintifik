import pandas as pd

# Nama file CSV yang akan dimodifikasi
file_path = "data16.csv"

# Membaca data dari file CSV ke DataFrame
df = pd.read_csv(file_path)

# Menghapus baris dengan kondisi tertentu
df = df[df["Nama"] != "Alice"]

# Menyimpan DataFrame yang telah dimodifikasi kembali ke file CSV
df.to_csv(file_path, index=False)

print("Data telah dimodifikasi dan disimpan kembali ke", file_path)
