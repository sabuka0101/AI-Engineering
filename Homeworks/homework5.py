#Task 1

# scores = []

# scores.append(45)
# scores.append(88)
# scores.append(92)
# scores.append(60)
# scores.append(75)

# scores.remove(45)

# print(f"Scores {scores}")
# print(f"Avarage score {sum(scores) / len(scores)}")
# print(f"Highest score: {max(scores)}, Lowest: {min(scores)}")

# scores.sort()
# print(f"Sorted scores in ascending order: {scores}")

# passed_scores = []

# for score in scores:
#     if score >= 60:
#      passed_scores.append(score)
# print(f"Passed Scores: {passed_scores}")

#Task 2

# inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
# new_items = ["mango", "grape"]

# print(f"Counted apples: {inventory.count("apple")}")
# print(f"First orange index: {inventory.index("orange")}")
# inventory.extend(new_items)
# print(f"{inventory[::-1]}")

#Task 3

locations = [("Tbilisi", 41.71, 44.82), ("Batumi", 41.64, 41.63), ("Kutaisi", 42.26, 42.71)]
city_names = []

for city, latitude, longitude in locations:
   print(f"City: {city}, Latitude: {latitude}, Longitude: {longitude}")
   city_names.append(city)
print(f"City names: {city_names}")   