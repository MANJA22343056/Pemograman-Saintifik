hb = ["Programming in C#", ["Oxford University Press", 2015]]
rm = ["SE is everthing", ["Obscure Publishers", 2015]]
authors = [hb, rm]
print(authors)
print("List:\n" +str(authors[0]) + "\n" +str(authors[1] )+ "\n")
print("Name of books\n" + str(authors[0][0]) + "\n"+ str(authors[1][0]) +"\n" )
print("Detail of books\n" + str(authors[0][1]) + "\n" + str(authors[1][1])+"\n")
print("\nLevel 3 Publisher 1\t:" + str(authors[0][1][0]))