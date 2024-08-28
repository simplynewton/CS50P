cc = input("camelCase: ")
for c in cc: #for loop goes through each character in the string
    if c.isupper(): #checks if the character is uppercase
        c = c.lower() #converts the character to lowercase
        print("_"+c,end ="")
    else:
        print(c, end ="")
        