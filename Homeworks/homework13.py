# Task 1

# class MovieTicket:
#     cinema_name = "Rustaveli Cinema"
#     total_tickets_sold = 0

#     def __init__(self, movie_title, seat_number, price):
#         self.movie_title = movie_title
#         self.seat_number = seat_number
#         self.price = price
#         MovieTicket.total_tickets_sold += 1


# ticket1 = MovieTicket("Spider-Man", 15, 30)
# ticket2 = MovieTicket("Avengers", 17, 23)
# ticket3 = MovieTicket("Captain America", 12, 37)

# for ticket in [ticket1, ticket2, ticket3]:
#     print(
#         f"{ticket.cinema_name} | {ticket.movie_title} | Seat {ticket.seat_number} | {ticket.price} GEL"
#     )

# print(f"Total tickets sold: {MovieTicket.total_tickets_sold}")


# Task 2

# class User:
#     status = "Active"

#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.age = age

#     def get_info(self):
#         print(
#             f"Hello {self.username} you are {self.age} years old and your email is {self.email} and you are currently {self.status}"
#         )


# user1 = User("saba", "saba@gmail.com", 16)
# user2 = User("tazo", "tazo@gmail.com", 17)

# user1.get_info()
# user2.get_info()


# Task 3
class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity
        print(
            f"{quantity} {self.name}s had been sold and there are now {self.stock} in stock"
        )


product = Product("laptop", 200, 8)
product.sell(2)
