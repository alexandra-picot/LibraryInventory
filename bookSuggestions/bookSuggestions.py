strang = str(input("Enter a book you want to see in our library: "));
filename = open("bookSuggestions.txt","a");
filename.write(strang)
filename.write('\n')
filename.close()

filename2 = open("bookSuggestions.txt","r");
contents = filename2.read()
print("Book suggestions so far: ")
print(contents)
filename2.close()



