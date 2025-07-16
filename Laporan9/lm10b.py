lista = ["red", "green", "blue"]
listb = ["#FF0000", "#008000", "#0000FF"]

# pakai zip untuk menggabungkan dua list dan kemudian buat dictionary
kamusWarna = dict(zip(lista, listb))

print(kamusWarna)