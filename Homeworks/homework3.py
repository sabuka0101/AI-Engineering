#Task 1

# age = int(input("Enter your Age: "))

# if 0 < age < 5:
#     print("Your ticket is free")
# elif 5 <= age <= 12:
#     print("Your ticket price is 8$")
# elif 13 <= age <=64:
#     print("Your ticket price is 15$")
# elif age >= 65:
#     print("Your ticket price is 10$")
# elif age <= 0:
#     print("Error")

#Task 2

# cart_total = 50
# is_vip = False
# promo_code = "SAVE10"
# is_guest = False

# if cart_total >= 50 or is_vip:
#     print("You have Free Shipping")
# else:
#     print("You have to be either vip or get products above 50$ to get Free shipping")

# if promo_code == "SAVE10" and not is_guest:
#     print(f"You have a 10% discount and your total price is {cart_total - cart_total * 10/100}$")
# else:
#     print("you have to enter promo code and not be the guest to get 10% discount")

#Task 3 

correct_pin = 1234
balance = 200
requested_amount = 100

if correct_pin == int(input("Enter your pin: ")):
    print("Pin is correct")
    
    if balance >= requested_amount:
     print(f"Withdrawal successful! Remaining balance: {balance - requested_amount}")
else:
    print("Pin is wrong")