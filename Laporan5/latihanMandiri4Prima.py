def cekPrima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

angka = int(input("Masukkan sebuah bilangan: "))
if cekPrima(angka):
    print(angka, "adalah bilangan prima.")
else:
    print(angka, "bukan bilangan prima.")