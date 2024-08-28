def main():
    deep = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ")
    deep1 = deep.lower().replace(" ","")
    if deep1.find("42")!=-1:
     print ("Yes")
    elif deep1.find("fortytwo")!=-1:
     print ("Yes")
    elif deep1.find("forty-two")!=-1:
     print("Yes")
    else:
     print("No")
main()
