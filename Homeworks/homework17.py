import requests

# Task 1

BASE_URL = "https://crudcrud.com/api/51467d0a542a4b3cba7d01d60b76d79a"


# def post_request():
#     try:
#         product_data = {"name": "Laptop", "price": 2500, "in_stock": True}

#         response = requests.post(f"{BASE_URL}/products", json=product_data, timeout=10)
#         response.raise_for_status()
#         print(response.json())
#     except requests.exceptions.RequestException as error:
#         print(f"Request failed: {error}")


# post_request()

# Task 2


def get_request():
    try:
        response = requests.get(f"{BASE_URL}/products", timeout=10)
        response.raise_for_status()
        products = response.json()

        for product in products:
            print(
                f'Product name: {product["name"]}, Price: {product["price"]}, ID: {product["_id"]}'
            )
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


get_request()


# Task 3


def getBy_id(product_id):
    try:
        response = requests.get(f"{BASE_URL}/products/{product_id}", timeout=10)
        response.raise_for_status()
        product = response.json()
        print(f"Product name: {product["name"]}, Price: {product["price"]}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


def updateBy_id(product_id):
    updated_data = {"name": "Gaming Laptop", "price": 3200, "in_stock": True}
    try:
        response = requests.put(
            f"{BASE_URL}/products/{product_id}", json=updated_data, timeout=10
        )
        response.raise_for_status()
        print(f"Product {product_id} updated (status {response.status_code})")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


def deleteBy_id(product_id):
    try:
        response = requests.delete(f"{BASE_URL}/products/{product_id}", timeout=10)
        response.raise_for_status()
        print(f"Product {product_id} was deleted (status {response.status_code})")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


try:
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    response.raise_for_status()
    products = response.json()
    first_id = products[0]["_id"]

    getBy_id(first_id)
    updateBy_id(first_id)
    deleteBy_id(first_id)

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
