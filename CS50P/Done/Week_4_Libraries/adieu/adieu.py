user_names = []

while True:
    try:
        user_name = input()
        if user_name:
            user_names.append(user_name)

    except EOFError:
        break

if len(user_names) == 1:
    gb = f"Adieu, adieu, to {user_names[0]}"
elif len(user_names) == 2:
    gb = f"Adieu, adieu, to {user_names[0]} and {user_names[1]}"
else:
    gb ="Adieu, adieu, to " + ", ".join(user_names[:-1]) + ", and " + user_names[-1]
print(gb)




#user_names = []
#collects names until EOFError is encountered

#while True:
#    try:#repeats for input until stopped by EOFError
#        user_name = input("Name: ")
#        user_names.append(user_name)# add it to the end of the list.
#    except EOFError:
#        break
    #worked on this using vscode, just realized I could've connected to codespace :sob:
#if len(user_names) == 1:
#    gb = f"Adieu, adieu to {user_names[0]}"
#elif len(user_names) == 2:
#    gb = f"Adieu, adieu to {user_names[0]} and {user_names[1]}"
#^^^^ these 2 if statements handle the first 2 'fashions' that the code below can't handle
#else:
#    gb ="Adieu, adieu to " + ", ".join(user_names[:-1]) + "and ".join(user_names[-1]) # joins and to only the very last element

#print(gb)
