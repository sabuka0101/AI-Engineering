# Task 1


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(1234))

# Task 2

scores = [45, 82, 67, 38, 96, 55, 72]

passed_scores = list(filter(lambda n: n >= 50, scores))
bonus_point = list(map(lambda n: min(n + 5, 100), scores))

print(passed_scores)
print(bonus_point)

# Task 3

names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))
print(products)

by_price = sorted(products, key=lambda p: p[1], reverse=True)
print("By price (high → low):")
for name, price, rating in by_price:
    print(f"{name}: ${price}, rating {rating}")

by_rating = sorted(products, key=lambda p: p[2])
print("By rating (low → high):")
for name, price, rating in by_rating:
    print(f"{name}: ${price}, rating {rating}")
