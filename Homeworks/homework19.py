import requests
import time
import aiohttp
import asyncio

# Task 1

# BASE_URL = "https://jsonplaceholder.typicode.com/todos"

# time_start = time.time()

# for i in range(1, 11):
#     try:
#         res = requests.get(f"{BASE_URL}/{i}", timeout=5)
#         res.raise_for_status()
#         print(res.json())
#     except requests.exceptions.RequestException as error:
#         print(f"Request {i} failed: {error}")
# sync_time = time.time() - time_start
# print(f"request took {sync_time:.2f} seconds")


# async def fetch_todo(session, todo_id):
#     try:
#         async with session.get(f"{BASE_URL}/{todo_id}") as response:
#             response.raise_for_status()
#             return await response.json()
#     except (aiohttp.ClientError, asyncio.TimeoutError) as error:
#         print(f"Request {todo_id} failed: {error}")
#         return None


# async def main():
#     timeout = aiohttp.ClientTimeout(total=5)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         tasks = [fetch_todo(session, i) for i in range(1, 11)]
#         results = await asyncio.gather(*tasks)
#     for todos in results:
#         if todo:
#             print(todos)


# start = time.time()
# asyncio.run(main())
# async_time = time.time() - start
# print(f"aiohttp took {async_time:.2f} seconds")

# print(f"The async version was {sync_time - async_time:.2f} seconds faster!")

# Task 2

BASE_URL = " https://jsonplaceholder.typicode.com/posts"


async def fetch_posts(session, post_id):
    try:
        async with session.get(f"{BASE_URL}/{post_id}") as response:
            response.raise_for_status()
            return await response.json()
    except (aiohttp.ClientError, asyncio.TimeoutError) as error:
        print(f"Request {post_id} failed: {error}")
        return None


async def main():
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch_posts(session, i) for i in range(1, 21)]
        posts = await asyncio.gather(*tasks)
        user_posts = [post for post in posts if post["userId"] == 1]
        count = 1
    for post in user_posts:
        if post:
            print(f"{count}.{post["title"]}")
        count += 1


asyncio.run(main())
