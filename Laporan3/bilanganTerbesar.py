# input a, b, dan c
a = int(input("Masukkan bilangan pertama:"))
b = int(input("Masukkan bilangan pertama:"))
c = int(input("Masukkan bilangan pertama:"))

# secara berurutan tulis kriteria untuk a, b, dan c
if a > b and a > c:
    print("Terbesar: ", a)
elif b > a and b > c:
    print("Terbesar: ", b)
elif c > a and c > b:
    print("Terbesar: ", c)
