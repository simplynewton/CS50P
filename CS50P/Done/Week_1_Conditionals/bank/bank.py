def main():
    hello = input("Greting: ")
    hello1 =hello.lower()
    if hello1.find("hello")!=-1:
        print("$0")
    elif hello1.startswith("h") and hello1.find("hello")!=0:
        print("$20")
    else:
        print("$100")
main()
