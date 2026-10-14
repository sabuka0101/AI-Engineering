# Task 1


# def even_numbers():
#     count = 0
#     while True:
#         yield count
#         count += 2


# gen = even_numbers()

# for _ in range(10):
#     print(next(gen))

# Task 2

# words = ["python", "generator", "yield", "code", "ai", "developer"]

# cap_words = (word.upper() for word in words if len(word) > 4)

# for word in cap_words:
#     print(word)

# Task 3


def greeter_bot():
    while True:
        recieved = yield
        print(f"Hello {recieved}!")


gen = greeter_bot()
next(gen)

name = input("Enter your name: ")
gen.send(name)
