def main():
    greeting = input()
    print(value(greeting))

def value(greeting: str) -> int:# takes the string and outputs an integer
    #convert greeting to lowercase
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
