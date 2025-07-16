try:
    a = float(input("Masukkan sisi 1: "))
    b = float(input("Masukkan sisi 2: "))
    c = float(input("Masukkan sisi 3: "))

    if a == b == c:
        print("3 sisi sama")
    elif a == b or a == c or b == c:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Input tidak valid. Harap masukkan angka.")
