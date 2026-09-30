#Task 1
try:
 birth_year = int(input("Enter your birth year: "))
 print(f"You are {2026-birth_year} old")

except ValueError:
 print("Please enter only Digits!")

#Task 2
password = "saba123"

try:
 if len(password) < 6:
  raise ValueError("Password is too short!")

except ValueError as err:
 print(err)