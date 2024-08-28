def main():
    word = input()
    results = shorten(word)
    print(results)

def shorten(word):
    vowels = 'aeiouAEIOU'
    results = ""
    #to iterated through each letter of word
    for char in word:
        #to check if each iterated letter is in the vowel
        if char not in vowels:
            results += char

    return results #oops forgot to include

if __name__ == "__main__":
    main()
