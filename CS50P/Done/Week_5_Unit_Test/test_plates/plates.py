def main():
    plate = input()
    print(is_valid(plate)) # the code below str -> bool allows the print to be true or false

def is_valid(s: str) -> bool: # seems more efficient to do str -> bool
     #checks for periods, spaces, or punctuation marks
    pun = set(",.? !")
    # a setup for checking if the first number starts with 0
    i = 0
    for c in s:
        if c.isalpha():
            i+=1
        if c in pun:
            return False
    # checks if the plate has a minimum 2 letters and maximum of 6 characters
    if 2>len(s) or len(s) > 6:
        return False
    #checks if the plate starts with at least two letters
    if not s[0:2].isalpha():
        return False
    #checks if the plate is all alphabets
    for c in s:
        if s.isalpha():
            return True
        elif not s.isalpha():
    # checks if the first number = 0
            if s[i] =="0":
             return False
    # checks if there an alphabets AFTER the start of the first numbers
            elif any(c.isalpha() for c in s[i:] ):
              return False
    return True

if __name__ == "__main__":
    main()
