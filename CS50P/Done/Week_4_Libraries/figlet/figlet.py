import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figize("Input:", font)
    elif len(sys.argv) == 3:
        if sys.argv[1] =="-f" or sys.argv[1] == "--font":
            valid_fonts = figlet.getFonts()
            if sys.argv[2] not in valid_fonts:
                sys.exit("invalid usage")
            else:
                font = sys.argv[2]
                figize("Input:", font)
        else:
            sys.exit("invalid usage")
    else:
        sys.exit("invalid usage")

def figize(inpt, fant):
    int = input(inpt)
    figlet.setFont(font=fant)
    print("Output: ")
    print(figlet.renderText(int))


main()
