# name = input("What's your name? ")

# file = open("names.txt", "a") # the 'w' is a mode in open()
# file.write(f"{name}\n")
# file.close()

name = input("What's your name? ")
#  # The keyword 'with' allows you to automate the closing of a file.
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
# "r": Read (file must exist)
# "w": Write (creates file or truncates existing file)
# "a": Append (creates file or appends to existing file)
# "x": Exclusive creation (raises error if file exists)
# "b": Binary mode (used with other modes for binary files)
# "t": Text mode (default, used for text files)
# "r+": Read and write (file must exist)
# "w+": Write and read (creates file or truncates existing file)
# "a+": Append and read (creates file or appends to existing file)




# names = []

# for _ in range(3):
#     names.append(input("What's your name "))
#     #names.append(name)

# for name in sorted(names):
#     print(f"Hello, {name}")

