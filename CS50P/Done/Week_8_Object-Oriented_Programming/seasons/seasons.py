from datetime import date
import inflect
import sys

class Ageinmin:
    def __init__(self, bday, today = None):
        self.bday = self.parsedate(bday)
        self.today = today or date.today()
        self.mins = self.calcmin()

    def parsedate(self, bday):
        try:
            y, m, d = map(int, bday.split('-'))
            return date(y, m, d)
        except (ValueError, TypeError):
            raise ValueError("Invalid date format")

    def calcmin(self):
        delta = self.today - self.bday
        return delta.days*24*60

    def mintowords(self):
        p = inflect.engine()
        #replaces and with ""
        words = p.number_to_words(self.mins, andword="").replace('  ',' ')

        return f"{words} minutes".capitalize()

def main():
    bday = input("Date of Birth: ")
    try:
        Age_in_min = Ageinmin(bday)
        print(Age_in_min.mintowords())
    except ValueError:
        sys.exit("Invalid date format")

if __name__ == "__main__":
    main()
