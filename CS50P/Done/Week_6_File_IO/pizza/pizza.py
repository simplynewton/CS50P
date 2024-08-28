import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader) #The next() function is used to skip or separate the header row from the data rows.
            row = [row for row in reader] # https://stackoverflow.com/questions/27307385/best-way-to-access-the-nth-line-of-csv-file
            # source -> Is 'optimal' in terms of code compactness? Could do lines = [row for row in reader], then lines[N]. Note that like some other answers, this requires reading the whole file. –
            # CommentedDec 5, 2014 at 1:49
            table = tabulate(row, headers, tablefmt="grid")
        print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
