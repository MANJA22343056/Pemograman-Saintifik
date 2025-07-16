import csv

# Nama file CSV yang akan dibaca
file_path = "data_pisah_titik_koma.csv"

# Membuka file CSV dan membaca data dengan delimiter khusus
with open(file_path, "r") as file:
    # Menggunakan delimiter khusus (titik koma)
    reader = csv.reader(file, delimiter=";")

    # Membaca data baris per baris
    for row in reader:
        print(row)