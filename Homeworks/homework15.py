# Task 1
# def add_product(cart, product):
#     cart.append(product)
#     print(f"Added: {product}")


# def remove_last_product(cart):
#     if not cart:
#         print("Cart is empty")
#         return None
#     removed = cart.pop()
#     print(f"Popped: {removed}")
#     return removed


# def show_cart(cart):
#     print(f"Cart: {cart}")


# cart = []

# add_product(cart, "Milk")
# add_product(cart, "Bread")
# add_product(cart, "Cheese")
# add_product(cart, "Apple")
# show_cart(cart)

# remove_last_product(cart)
# show_cart(cart)
# Task 2
# users = ["gio", "nino", "gio", "ana", "nika", "ana"]


# def users_set(users):
#     return set(users)


# print(users_set(users))

# Task 3
dictionary = {
    "giorgi": "599123456",
    "ana": "591123456",
    "nika": "555123456",
    "mariami": "577123456",
}


def find_user(dictionary):
    return dictionary.get("giorgi", "Not in the dictionary")


print(find_user(dictionary))
