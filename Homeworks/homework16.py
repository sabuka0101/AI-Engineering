# Task 1
from dataclasses import dataclass, asdict
import json


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


product1 = Product("Laptop", 2000.0, True)
product2 = Product("Phone", 800.0, False)
product3 = Product("Headphones", 150.0, True)

dict_product = asdict(product1)

json_text = json.dumps(dict_product, indent=4)

print(json_text)
print(product2)
print(product3)

# Task 2

json_text = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data = json.loads(json_text)
print(data)
print(type(data))

p = Product(**data)

print(type(p))
print(p.name)
print(p.price)
print(p.in_stock)
