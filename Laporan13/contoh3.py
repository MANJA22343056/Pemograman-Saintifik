import csv

# Nama file CSV yang akan dibaca
file_path = "data16.csv"

# Membuka file CSV dan membaca data menggunakan csv.reader
with open(file_path, "r") as file:
    reader = csv.reader(file)

    # Membaca data sebagai list sebelum file ditutup
    data_as_list = list(reader)

print("Data sebagai list:")
for row in data_as_list:
    print(row)