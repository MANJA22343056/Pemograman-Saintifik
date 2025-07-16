import csv

# Nama file CSV yang akan ditulis
file_path_list = "output_list.csv"

# Data dalam bentuk list
data_to_write_list = [
    ["Nama", "Usia", "Kota"],
    ["John", 25, "New York"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 28, "Los Angeles"],
]

# Membuka file CSV dan menulis data menggunakan csv.writer
with open(file_path_list, "w", newline="") as file_list:
    writer_list = csv.writer(file_list)

    # Menulis data dari list ke file CSV
    writer_list.writerows(data_to_write_list)

print(f"Data dari list berhasil ditulis ke {file_path_list}")