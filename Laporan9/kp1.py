# 1) membuat dan mencetak tuple

kota = ("jakarta", "jogja", "surabaya")
print("kota: ", kota)
print("kota[0]: ", kota[0])
print("kota[1]: ", kota[1])
print("kota[2]: ", kota[2])
print()

# 2) membagi tuple kedalam string
str1, str2, str3 = kota
print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)
print()

# 3) membuat tuple yang berisi string dari sebuah kata

tpl = tuple ("belajar python")
print("tpl:", tpl)
print(tpl)

# 4) membuat tuple yang berisi semua, kecuali huruf pertama dari sebuah string

# direct string
tpl1 = tuple ("belajar python"[1:])
print("tpl1: ", tpl1)

# 5) mencetak tiple secara terbaik

name = ("jaka", "joko", "jono")

#using slicing technique
revName = name[::-1]
rev2 = name[::2]
print("urutan: ", name)
print("urutan terbali: ", revName)