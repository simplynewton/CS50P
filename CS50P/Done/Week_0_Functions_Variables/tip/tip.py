def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print (f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.replace("$", "")
    dtf = float(d)
    return dtf
def percent_to_float(p):
    p = p.replace ("%","")
    pts = float(p)/100
    return pts

main()
