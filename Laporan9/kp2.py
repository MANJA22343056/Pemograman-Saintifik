dicEmail = dict()
lst = list()

fname = input("nama file: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("file cannot be opened: ", fname)
    exit()

for baris in fhand:
    kata = baris.split()
    if len(kata) < 3 or kata[0] != "From":
        continue
    else:
        if kata[2] not in dicEmail:
            dicEmail[kata[2]] = 1
        else:
            dicEmail[kata[2]] += 1

for key, val in list(dicEmail.items()):
    lst.append((val,key))
    
lst.sort(reverse= True)

for key, val in lst[:1]:
    print(val,key)