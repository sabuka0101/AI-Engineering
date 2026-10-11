# Task 1


# def make_counter(start_value=0):
#     def closure():
#         nonlocal start_value
#         start_value += 1
#         return start_value

#     return closure


# counter = make_counter(start_value=10)
# print(counter())
# print(counter())
# print(counter())

# Task 2

# from functools import wraps
# import time


# def log_execution(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(
#             f"Running {func.__name__}... Executed in {end_time - start_time:.2f} seconds"
#         )
#         return result

#     return wrapper


# @log_execution
# def add(a, b):
#     """Adds two numbers."""
#     time.sleep(1)
#     return a + b


# print(add(3, 5))
# print(add.__doc__)
# print(add.__name__)

# Task 3


def require_role(allowed_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role")
            if allowed_role == user_role:
                return func(*args, **kwargs)
            else:
                return "Permission Denied: User is not an admin"

        return wrapper

    return decorator


@require_role(allowed_role="admin")
def check_role(user_role):
    return "Welcome admin"


print(check_role(user_role="admin"))
print(check_role(user_role="guest"))
