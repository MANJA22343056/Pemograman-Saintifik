hb = ["Programming in C#", ["Oxford University Press", 2015]]
rm = ["SE is everthing", ["Obscure Publishers", 2015]]
authors = [hb, rm]
print(authors)
for i in range(len(authors)):
    for j in range(len(authors[i])):
        print(str(i)+" "+str(j)+" "+str(authors[i][j])+"\n")