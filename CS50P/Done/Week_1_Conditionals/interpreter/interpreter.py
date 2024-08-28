def main():
    expression = input("Expression: ")
    pl = expression.split(" ")
    x = float(pl[0])
    y = pl[1]
    z = float(pl[2])
    if y == "-":
      print (x-z)
    elif y =="+":
        print (x+z)
    elif y == "*":
        print (x*z)
    elif y =="/":
        print(x/z)
main()
