import sys
import csv

def main():
    #conditions before able to try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[2].endswith(".csv") or sys.argv[3].endswith(".csv")):
        sys.exit("Not a CSV file")

    ffile = sys.argv[1] #before file
    sfile = sys.argv[2] #after file

    try:
        with open(ffile,'r')as csvfile:
            reader = csv.DictReader(csvfile)
            rows = []
            for row in reader:
                #splits the 'name' field into first and last
                lname, fname = row['name'].split(', ')
                rows.append({"first":fname,"last":lname,"house":row['house']})# keep house the same
    except FileNotFoundError:
        sys.exit("File not found")
    with open(sfile,'w', newline='') as outfile:
        field = ['first','last','house']
        writer = csv.DictWriter(outfile, fieldnames=field)
        writer.writeheader()
        writer.writerows(rows)
if __name__ == "__main__":
    main()
