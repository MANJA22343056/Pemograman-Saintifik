import csv

# Nama file CSV yang akan ditulis
file_path_tuple = "output_tuple.csv"

# Data dalam bentuk tuple
data_to_write_tuple = [
    ["Nama", "Usia", "Kota"],
    ["John", 25, "New York"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 28, "Los Angeles"],
]

# Membuka file CSV dan menulis data menggunakan csv.writer
with open(file_path_tuple, "w", newline="") as file_tuple:
    writer_tuple = csv.writer(file_tuple)

    # Menulis data dari tuple ke file CSV
    writer_tuple.writerows(data_to_write_tuple)

print(f"Data dari tuple berhasil ditulis ke {file_path_tuple}")
