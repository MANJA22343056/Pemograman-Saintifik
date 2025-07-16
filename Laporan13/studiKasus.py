import csv

def load_contacts():
    try:
        with open('contacts.csv') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.csv', 'w', newline='') as file:
        fieldnames = ['ID', 'Nama', 'Nomor Telepon', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    # Mintalah pengguna memasukkan informasi kontak baru
    nama = input("Masukkan nama kontak: ")
    nomor_telepon = input("Masukkan nomor telepon kontak: ")
    email = input("Masukkan email kontak: ")
    
    # Hitung ID baru untuk kontak
    if contacts:
        latest_id = max(int(contact['ID']) for contact in contacts)
        new_id = latest_id + 1
    else:
        new_id = 1
    
    # Tambahkan kontak baru ke dalam daftar
    new_contact = {'ID': new_id, 'Nama': nama, 'Nomor Telepon': nomor_telepon, 'Email': email}
    contacts.append(new_contact)
    print("Kontak baru berhasil ditambahkan.")

def search_contact(contacts, search_name):
    found_contacts = [contact for contact in contacts if contact['Nama'].lower() == search_name.lower()]
    if found_contacts:
        print("Kontak ditemukan:")
        for contact in found_contacts:
            print("ID:", contact['ID'])
            print("Nama:", contact['Nama'])
            print("Nomor Telepon:", contact['Nomor Telepon'])
            print("Email:", contact['Email'])
    else:
        print("Kontak tidak ditemukan.")

def main():
    contacts = load_contacts()

    while True:
        print("Menu Program:")
        print("1. Tambah Kontak Baru")
        print("2. Cari Kontak")
        print("3. Keluar")

        choice = input("Pilih menu (1/2/3): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_name = input("Masukkan nama yang ingin dicari: ")
            search_contact(contacts, search_name)
        elif choice == '3':
            save_contacts(contacts)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()