def main():
    d = dict()
    while True:
        try:
            key = input().upper()
            d[key] = d.get(key, 0) + 1
        except EOFError:
            break
    sorted_items = sorted(d.items())
    for key, value in sorted_items:
        print(f"{value} {key}")
main()
