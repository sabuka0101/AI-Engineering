#Task 1

first_name = input("First name: ")
last_name = input("Last name: ")

first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
print(first_name, last_name)

#Task 2

text = "My favorite thing is Python"

print(text.replace("thing", "language"))
print(text.find("Python"))
print(text[12:])

#Task 3

name = input("Enter your Name: ")
company = input("Enter your Company: ")

print(f"Hello {name.capitalize()}, your Workspace is {company.capitalize()}")