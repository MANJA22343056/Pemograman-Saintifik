import csv

# Nama file CSV yang akan ditulis
file_path = "output_khusus_delimiter.csv"

# Data yang akan ditulis
data_to_write = [
    ["Nama", "Usia", "Kota"],
    ["John", 25, "New York"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 28, "Los Angeles"],
]

# Membuka file CSV dan menulis data dengan delimiter khusus
with open(file_path, "w", newline="") as file:
    # Menggunakan delimiter khusus (titik koma)
    writer = csv.writer(file, delimiter=";")

    # Menulis data ke file CSV
    writer.writerows(data_to_write)

print("Data dengan delimiter khusus berhasil ditulis ke", file_path)
