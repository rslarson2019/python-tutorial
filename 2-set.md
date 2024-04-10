# SETS

In Python, a set is an unordered collection of unique elements. It is implemented as a hash table which provides highly efficient membership tests
and eliminates duplicate entries. Sets are mutable, meaning you can add or remove elements from them.

## Why we use sets

Sets are used when you need to store a collection of distinct elements and perform operations like intersection, union, difference, and symmetric
difference efficiently. They are particularly useful in scenarios where you need to eliminate duplicates from a collection or check for membership.

## How to use sets:

You can create a set in Python by enclosing comma-separated elements within curly braces `{}` or by using the `set()` constructor. To add elements
to a set, you can use the `add()` method. To remove elements, you can use the `remove()` or `discard()` methods. Sets support various operations
like union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`), etc.

## Big O Notation

The set data structure contributes to code efficiency by providing several key advantages:

**Fast Lookup:** Sets offer constant-time average case lookup for elements, making them ideal for scenarios where quick membership tests are
required. This efficiency is particularly beneficial for tasks like duplicate elimination or checking for existence.

**Ordered Operations:** Some implementations of sets, such as ordered sets or sorted sets, maintain elements in a specific order. This allows for
efficient iteration over elements in sorted order, facilitating tasks like range queries or finding nearest neighbors.

**Deduplication:** Sets automatically eliminate duplicate elements, ensuring that only unique values are stored. This can lead to memory savings
and improved performance, especially when dealing with large datasets.

**Intersection and Union Operations:** Sets support efficient intersection, union, and difference operations, enabling complex set-based
computations with minimal overhead.

**Hash-Based Implementation:** Many set implementations use hash tables for efficient storage and retrieval of elements. Hash tables offer
average-case constant-time performance for insertion, deletion, and lookup operations, making sets suitable for a wide range of applications.

### Example Problem 1:

Let's say we have two sets representing the students enrolled in Math and Physics classes. We want to find out:

1. How many students are enrolled in both Math and Physics classes?
2. List the students who are only enrolled in one of the classes.

### Expected Results
Output:
Number of students enrolled in both Math and Physics: 2
Students enrolled only in Math: {'Bob', 'Alice'}
Students enrolled only in Physics: {'Eve', 'Frank'}

Please see [Link to Python Script](set.py) for the answers

### Example Problem 2:
Consider a scenario where you have a list of colors, and you want to remove duplicate colors from the list and sort them alphabetically. How would you achieve this using sets?

### Expected Results
Output:
Unique sorted colors: ['blue', 'green', 'red', 'yellow']
In this example, the set automatically eliminates duplicates, and using `sorted()`, we ensure that the colors are sorted alphabetically.

Please see [Link to Python Script](set.py) for the answers

### Real world example problem

You need to manage a list of ingredients in a kitchen pantry and a shopping list of ingredients needed to prepare a set of recipes.

Suppose you have the following data:

List of ingredients in the kitchen pantry.
List of ingredients needed to prepare each recipe.
List of ingredients currently available in the shopping list.
Your task is to find out:

Ingredients needed to prepare a specific recipe that are not available in the kitchen pantry.
Ingredients that need to be added to the shopping list to prepare a set of recipes.

### Expected Results 

Ingredients needed for the selected recipe that are not in the pantry: {'salt'}
Ingredients to add to the shopping list for the set of recipes: {'butter', 'flour', 'salt'}

Please see [Link to Python Script](set.py) for the answers