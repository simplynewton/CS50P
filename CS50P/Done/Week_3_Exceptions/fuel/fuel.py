def main():
     while True:
        try:
            Z = input("Fraction:")
            x, y = Z.split("/")
            x = int(x)
            y = int(y)
            percent = (x/y) * 100
            if x >y:
                raise ValueError

        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            if percent <=1:
                print("E")
                break
            elif percent >=99:
                print("F")
                break
            else:
                print(f"{round(percent)}%")
                break
main()
