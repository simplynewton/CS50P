def main():
    twh = convert(input("What time is it? "))
    if twh >=7 and twh <= 8:
         print("breakfast time")
    elif twh >= 12 and twh <= 13:
        print("lunch time")
    elif twh >= 18 and twh <= 19:
        print("dinner time")

def convert(time):
    if any(sub in time for sub in ["a.m.","a.m","am"]):
        time = time.replace("a.m.","").replace("a.m","").replace("am","").lower()
        hours, minutes = time.split(":")
        minutes = float(minutes)/60.0
        hours = float(hours)
        time = hours + minutes
        return float(time)



    elif any(sub in time for sub in ["p.m.","p.m","pm"]):# any(function) checks
        time = time.replace("p.m.", "").replace("p.m","").replace("pm","").lower()
        hours, minutes = time.split(":")
        minutes = float(minutes)/60.0
        hours = float(hours)
        time = hours + minutes + 12


        print(time)
        return float(time)

    else:
        hours, minutes = time.split(":")
        time = time.replace(":", "")
        minutes = float(minutes)/60.0
        hours = float(hours)
        time = hours + minutes
        return float (time)
        print(time)

if __name__ == "__main__":
    main()
print (__name__)
