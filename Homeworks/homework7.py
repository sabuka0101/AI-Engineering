# Task 1

# frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
# backend_skills = {"Python", "JavaScript", "SQL", "React"}

# print(frontend_skills | backend_skills)
# print(frontend_skills & backend_skills)
# print(frontend_skills - backend_skills)
# print(frontend_skills ^ backend_skills)

# Task 2

# student = {
#     "name": "ana",
#     "contacts": {"phone": "599123456", "email": "ana@gmail.com"},
#     "courses": {"course": "python", "score": 50, "passed": False},
# }

# print(f"{student["name"].capitalize()}'s email: {student["contacts"]["email"]}")
# print(f"{student["courses"]["course"]} score: {student["courses"]["score"]}")

# student["courses"].update({"course": "web", "score": 65, "passed": True})
# del student["contacts"]["phone"]
# print(student)

# Task 3

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]

word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print(word_counts)
