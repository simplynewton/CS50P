def main():
     while True:
        try:
            Z = convert(str(input()))
        except(ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(Z))
            break

def convert(fraction: str)-> int:
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y ==0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        percentage = (x/y) * 100
        return percentage

    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage: int) -> str:
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage}%"
if __name__ == "__main__":
    main()
