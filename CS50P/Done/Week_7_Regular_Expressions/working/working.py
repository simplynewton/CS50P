import re

def convert (s):
    # to match time format
    match = re.match(r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)', s)

    if not match:
        raise ValueError

    #extract the groups
    shour, smin, speriod, ehour, emin, eperiod = match.groups()

    start24 = convertto24(shour, smin, speriod)
    end24 = convertto24(ehour, emin, eperiod)
    return f"{start24} to {end24}"

def convertto24(hour, min, period):
    hour = int(hour)
    min = int(min or 0) # to handle cases where minute == 0

    if not(1<= hour <= 12):
        raise ValueError
    if not(0<= min < 60):
        raise ValueError


    if period == "AM":
        if hour == 12: #midnight case
            hour = 0
    if period == "PM":
        if hour !=12: #noon case
            hour +=12


    return f"{hour:02}:{min:02}"

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
