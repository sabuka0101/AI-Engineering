#First Exercise

String = "Hello World!"
Integer = 16
Float = 5.2
Boolean = True

print(type(String))
print(type(Integer))
print(type(Float))
print(type(Boolean))

#Second Exercise

age = int(input("Enter your birth year: "))

print(f"You are {2026 - age} years old")

#Third Exercise

number = int(input("Enter a number: "))

print("Positive:", number > 0)
print("Negative:", number < 0)
print("Zero:", number == 0)
print("Even:", number % 2 == 0)
print("Odd:", number % 2 != 0)