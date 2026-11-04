import time
import requests
from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor

# Task 1

# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result


# if __name__ == "__main__":
#     numbers = [40000, 40000, 40000, 40000]

#     start = time.time()
#     for n in numbers:
#         factorial(n)
#     single_time = time.time() - start
#     print(f"Single-process - time: {single_time:.2f} seconds")

#     start = time.time()
#     with Pool() as pool:
#         pool.map(factorial, numbers)
#     multi_time = time.time() - start
#     print(f"Multiprocessing - time: {multi_time:.2f} seconds")

#     print(f"Multiprocessing is {single_time / multi_time:.1f} times faster")

# Task 2

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_post(post_id):
    response = requests.get(f"{BASE_URL}/{post_id}", timeout=10)
    print(f"Post {post_id} done")


start = time.time()

threads = []
for i in range(1, 101):
    thread = threading.Thread(target=fetch_post, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_time = time.time() - start

print(f"Total time: {total_time:.2f} seconds")

# Task 3

start1 = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch_post, range(1, 101))

total_time1 = time.time() - start1

print(f"done in {total_time1:.2f}")
print(f"{total_time/total_time1:.2f} times faster")
