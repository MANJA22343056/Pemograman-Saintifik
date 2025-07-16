def cekDuplikat(string):
    karakterSet = set()
    
    for karakter in string:
        if karakter in karakterSet:
            return True
        else:
            karakterSet.add(karakter)
            
        return False
    
string1 = 'manja hebat'
print(cekDuplikat(string1))

string2 = 'MANJA'
print(cekDuplikat(string2))