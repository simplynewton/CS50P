def main():
    d = dict({"baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00})
    total = 0
    while True:
        try:
            key = input("Item: ").lower()
            if key in d:
                total+=d[key]
                total = float(total)
                print(f"${total:.2f}")
        except EOFError:
            break
        except KeyError:
            pass
main()

