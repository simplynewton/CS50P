import re
email = input("What's your gmail").strip()

username, domain = email.split("@")

if re.search(r".+@.+\.edu$", email):
    print("Valid")
else:
    print("Valid")

# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invlaid")
