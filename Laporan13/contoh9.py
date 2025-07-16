import pandas as pd

# Nama file CSV yang akan dimodifikasi
file_path = "data16.csv"

# Membaca data dari file CSV ke DataFrame
df = pd.read_csv(file_path)

# Menambahkan baris baru
new_row = {"Nama": "Eva", "Usia": 27, "Kota": "Chicago"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Menyimpan DataFrame yang telah dimodifikasi kembali ke file CSV
df.to_csv(file_path, index=False)

print("Data telah dimodifikasi dan disimpan kembali ke", file_path)
