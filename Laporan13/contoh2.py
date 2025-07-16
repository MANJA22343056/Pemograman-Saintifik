import csv

# Nama file CSV yang akan ditulis
file_path = "output.csv"

# Data yang akan ditulis
data_to_write = [
    ["Nama", "Usia", "Kota"],
    ["John", 25, "New York"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 28, "Los Angeles"],
]

# Membuka file CSV dan menulis data menggunakan csv.writer
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    # Menulis data ke file CSV
    writer.writerows(data_to_write)

print("Data berhasil ditulis ke", file_path)