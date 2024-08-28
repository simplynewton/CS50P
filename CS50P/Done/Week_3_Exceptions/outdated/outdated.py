
months = dict(
    {"January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12})
while True:
    try:
        uscal = input("Date: ")
        if " " in uscal and "/" in uscal:
            uscal = uscal.strip()
        # checks if input is in MM/DD/YYYY format
        if uscal[0].isdigit():
            m, d, y = uscal.split("/")
            d = int(d)
            y = int(y)
            m = int(m)
            if d >= 32 or m >=13: #check if the date is "valid"
                raise ValueError
            else:
                print(f"{y}-{m:02}-{d:02}") # :02 will format an integer as a two-digit number
        # checks if input is middle-endian format
        elif uscal[0].isalpha():
            if "," not in uscal:
                raise ValueError
            else:
                m, d, y = uscal.split(" ")
                d = d.replace(",","")
                m = m.title()
                m = int(months[m])
                d = int(d)
                y = int(y)
                if d >= 32 or m >=13:
                    raise ValueError
                else:
                    print(f"{y}-{m:02}-{d:02}")
    except ValueError:
        pass
    else:
        break
