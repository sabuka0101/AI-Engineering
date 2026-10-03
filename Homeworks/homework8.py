# Task 1

# def create_user_profile(first_name, last_name, role="Student", is_active=True):
#     user_profile = {
#         "First name": first_name,
#         "Last name": last_name,
#         "Role": role,
#         "Active": is_active,
#     }
#     return user_profile


# create_user_profile("saba", "shavbalaxashvili")

# Task 2

# def add_task(task_name, task_list=[]):
#     task_list.append(task_name)
#     return task_list


# print(add_task("Wash the dishes"))
# print(add_task("Clean room"))
# print(add_task("Take out trash"))

# ეს ყველა დავალება ერთი და იმავე ლისტში იმიტოა რადგან თვითონ ეს ლისტი არის default პარამეტრი.


# def add_task(task_name, task_list=None):
#     if task_list is None:
#         task_list = []
#     task_list.append(task_name)
#     return task_list


# print(add_task("Wash the dishes"))
# print(add_task("Clean room"))
# print(add_task("Take out trash"))

# ამ მაგალითზე ყოველ ფუნქციის გაშვებაზე ხელ ახლა იქმნება ლისტი, შესაბამისად ცალ ცალკე იპრინტება დავალებები.

# Task 3


def analyze_text(text, min_length=3, ignore_stopwords=None):

    if ignore_stopwords is None:
        ignore_stopwords = ""
    words = text.split()
    count = 0

    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1
    return count


print(analyze_text("I love the sea and the sun"))
print(analyze_text("I love the sea and the sun", min_length=4))
print(analyze_text("I love the sea and the sun", ignore_stopwords=["the", "and"]))
