# Task 1


# def user_input():
#     writer = input("Enter your favorite writer: ")
#     quote = input("Enter your favorite quote: ")
#     with open("quotes.txt", "w") as file:
#         file.writelines([f"{writer}\n", quote])


# user_input()


# def read_file():
#     with open("quotes.txt", "r") as file:
#         return file.read()


# print(read_file())

# Task 2

# import csv


# def get_survivors():
#     with open("titanic.csv") as file:
#         rows = list(csv.DictReader(file))
#     return [row for row in rows if row["survived"] == "1"]


# def save_survivors(survivors):
#     with open("survived.csv", "w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=survivors[0].keys())
#         writer.writeheader()
#         writer.writerows(survivors)


# survivors = get_survivors()
# save_survivors(survivors)

# Task 3

import csv


def read_employees():
    with open("ssl_companies.csv", "r") as file:
        rows = list(csv.DictReader(file))
    return [row for row in rows if int(row["employees"]) > 1000]


def sorted_ssl(employees):
    with open("sorted_ssl.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)


employees = read_employees()
sorted_ssl(employees)
