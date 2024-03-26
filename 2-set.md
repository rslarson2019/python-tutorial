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

### Example Problem 1:

Let's say we have two sets representing the students enrolled in Math and Physics classes. We want to find out:

1. How many students are enrolled in both Math and Physics classes?
2. List the students who are only enrolled in one of the classes.

### Expected Results
Output:
Number of students enrolled in both Math and Physics: 2
Students enrolled only in Math: {'Bob', 'Alice'}
Students enrolled only in Physics: {'Eve', 'Frank'}

### Example Problem 2:
Consider a scenario where you have a list of colors, and you want to remove duplicate colors from the list and sort them alphabetically. How would you achieve this using sets?

### Expected Results
Output:
Unique sorted colors: ['blue', 'green', 'red', 'yellow']
In this example, the set automatically eliminates duplicates, and using `sorted()`, we ensure that the colors are sorted alphabetically.