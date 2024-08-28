def main():
   #dict that matches an item with its calories(Matching Values)
    fruit = {"apple":"130",
        "avocado":"50",
        "banana":"110",
        "cantaloupe":"50",
        "grapes":"90",
        "honeydewmelon":"50",
        "kiwifruit":"90",
        "lemon":"15",
        "lime":"20",
        "nectarine":"60",
        "orange":"80",
        "peach":"60",
        "pear":"100",
        "pineapple":"50",
        "plums":"70",
        "starwberries":"50",
        "sweetcherries":"100",
        "tangerine":"50",
        "watermelon":"80"}

    fruitchecker = input("Item: ").replace(" ","").lower()

    #looks for inputed item
    if fruitchecker in fruit:
        print("Calories:", fruit[fruitchecker])

main()
