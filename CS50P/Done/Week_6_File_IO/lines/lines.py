import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filepath = sys.argv[1]
    if not filepath.endswith(".py"):
        sys.exit("Not a Python File")
    number_of_lines = LOC(filepath)
    print(number_of_lines)

def LOC(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    linesofcode = 0
    inside_docstring = False

    for line in lines:
        stripped_line = line.strip()
            #SO Depressed, miss read doc string lines, and i thought we should exlud it but I wan't suppose too 

        if not stripped_line or stripped_line.startswith('#'):
            continue

        # now that the lines are filtered
        linesofcode +=1
    return linesofcode

if __name__ == '__main__':
    main()
