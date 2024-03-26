# Example Problem 1 Answer

math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Charlie", "David", "Eve", "Frank"}
# How many students are enrolled in both Math and Physics classes?
common_students = len(math_students & physics_students)
print("Number of students enrolled in both Math and Physics:", common_students)
# List the students who are only enrolled in one of the classes.
only_math_students = math_students - physics_students
only_physics_students = physics_students - math_students
print("Students enrolled only in Math:", only_math_students)
print("Students enrolled only in Physics:", only_physics_students)


# Additional Example Problem:
colors = ["red", "blue", "green", "red", "yellow", "blue"]
unique_colors = sorted(set(colors))
print("Unique sorted colors:", unique_colors)

