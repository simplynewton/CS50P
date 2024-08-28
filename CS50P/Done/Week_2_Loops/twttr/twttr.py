

tw = input("Input: ")
vowels = set("aeiouAEIOU") #geekforgeeks | set() function
print("Output: ", end = "")
for c in tw:
    if c in vowels:
        print("", end = "")
    else:
        print(c, end ="")

