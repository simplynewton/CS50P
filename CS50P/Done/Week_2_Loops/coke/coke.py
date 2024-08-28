amd = 50
while amd > 0 or amd <= 0:
    if amd > 0:
        print("Amount Due:", amd)
        due = int(input("Insert Coins:"))
        if due == 25:
            amd -=  25
        elif due == 10:
            amd -= 10
        elif due == 5:
            amd -= 5
    elif amd <=0:
        od = amd*-1
        print("Change Owed:",od)
        break
