satu = "Step! on, no..pets??"
satu = satu.lower()

satu =''.join([i for i in satu if i.isalpha()])

dua = satu[::-1]
if dua == satu:
    print("palindrom")
else:
    print("bukan")