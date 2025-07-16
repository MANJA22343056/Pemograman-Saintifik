dictionaryDays = dict()
fname = input("enter a file name:")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("file cannot be opened: ", fname)
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] !="From":
        continue
    else:
        if words[2] not in dictionaryDays:
            dictionaryDays[words[2]] = 1
        else:
            dictionaryDays[words[2]] += 1
            
print(dictionaryDays)