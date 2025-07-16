fname = input("enter the file name: ")
try:
    fhand = open(fname)
except:
    print("file cannot be opened: ", fname)
    exit()
    
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
            
print(counts)