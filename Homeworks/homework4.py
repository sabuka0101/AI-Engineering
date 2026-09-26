#Task 1

# correct_pin = 1234

# attempts = 3

# while attempts > 0:
#     pin = int(input("Enter pin: "))
#     attempts -= 1
#     if pin == correct_pin:
#             print("Pin is correct")
#             break
#     elif attempts > 0:
#          print(f"Wrong pin, attempts remaining {attempts}")
#     else:
#           print("You are out of attempts")
#           break

#Task 2

# num = int(input("Enter positive number: "))
# sum = 0

# if num < 0 :
#       print("Number should be positive")
# else:
#  for i in range(1, num+1):
#         if i % 2 == 0:
#             sum += i
#  print(f"the sum of even numbers from 1 to {num} is {sum}")

#Task 3 

userText = input("Enter random text with number: ")

text = ""

for i in userText:
    if i.isdigit():
        continue
    text += i
print(text)