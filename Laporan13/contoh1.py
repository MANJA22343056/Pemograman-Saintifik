import csv

# Nama file CSV yang akan dibaca
file_path = "data16.csv"

# Membuka file CSV dan membaca data menggunakan csv.reader
with open(file_path, "r") as file:
    reader = csv.reader(file)

    # Mengakses data baris per baris
    for row in reader:
        print(row)