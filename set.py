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

# Real world example problem

# Define ingredients in the kitchen pantry
pantry = {"flour", "sugar", "eggs", "milk", "butter", "salt"}

# Define ingredients needed for each recipe
recipe_1 = {"flour", "sugar", "eggs", "butter"}
recipe_2 = {"milk", "sugar", "eggs", "butter"}
recipe_3 = {"flour", "sugar", "eggs", "milk", "salt"}

# Define ingredients currently available in the shopping list
shopping_list = {"milk", "sugar", "salt"}

# Specify the recipe for which we want to check the needed ingredients
selected_recipe = recipe_3

# Find ingredients needed to prepare the selected recipe that are not available in the kitchen pantry
needed_ingredients = selected_recipe.difference(pantry)
print("Ingredients needed for the selected recipe that are not in the pantry:", needed_ingredients)

# Find ingredients to add to the shopping list to prepare a set of recipes
recipes = [recipe_1, recipe_2, recipe_3]
ingredients_for_recipes = set().union(*recipes)
additional_ingredients = ingredients_for_recipes.difference(pantry.union(shopping_list))
print("Ingredients to add to the shopping list for the set of recipes:", additional_ingredients)
