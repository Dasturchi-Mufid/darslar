# Dictionary

# capital_city = {"O`zbekiston": "Tashkent", "Italy": "Rome", "England": "London"}
# print(capital_city["O`zbekiston"])

# # dictionary with keys and values of different data types
# numbers = {1: "One", 2: "Two", 3: "Three"}
# print(numbers)

# capital_city = {"O`zbekiston": "Tashkent", "England": "London"}
# print("Initial Dictionary: ",capital_city)

# capital_city["Japan"] = "Tokyo"

# print("Updated Dictionary: ",capital_city)

# student_id = {111: "Akramjon", 112: "Xurshid", 113: "Nurbek"}
# print("Initial Dictionary: ", student_id)

# student_id[112] = "Sultonbek"

# print("Updated Dictionary: ", student_id)

# student_id = {111: "Islombek", 112: "Sayydobek", 113: "Mansur"}

# print(student_id[111])  # prints Islombek
# print(student_id[113])  # prints Mansur

# student_id = {111: "Islombek", 112: "Sayyodbek", 113: "Mansur"}
# print(student_id[211])  

# # Output: KeyError: 211

# student_id = {111: "Islombek", 112: "Sayyodbek", 113: "Mansur"}

# print("Initial Dictionary: ", student_id)

# del student_id[111]

# print("Updated Dictionary ", student_id)

# student_id = {111: "Islombek", 112: "Sayyodbek", 113: "Mansur"}

# # delete student_id dictionary
# del student_id

# print(student_id)

# # Output: NameError: name 'student_id' is not defined

# # Membership Test for Dictionary Keys
# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# # Output: True
# print(1 in squares) # prints True

# print(2 not in squares) # prints True

# # membership tests for key only not value
# print(49 in squares) # prints False

# Iterating through a Dictionary
# squares = {1: 1,  7: 49, 5: 25, 3: 9, 9: 81}
# for i in squares:
#     print(squares[i])

# Methods and Functions
# print(len(squares))
# print(sorted(squares))
# print(squares.clear())

# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# print(squares.keys())
# print(squares.values())