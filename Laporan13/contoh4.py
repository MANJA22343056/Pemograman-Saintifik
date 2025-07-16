import csv

# Nama file CSV yang akan dibaca
file_path = "data16.csv"

# Membuka file CSV dan membaca data menggunakan csv.reader
with open(file_path, "r") as file:
    reader = csv.reader(file)

    # Membaca data sebagai tuple
    data_as_tuple = [tuple(row) for row in reader]

print("Data sebagai tuple:")
for row in data_as_tuple:
    print(row)