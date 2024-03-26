# Introduction to Trees

A tree is a hierarchical data structure composed of nodes. Each node contains a value and a list of references to its child nodes. The topmost
node is called the root node, and each node in the tree is connected by edges.

## Why Use Trees?
Trees are widely used in computer science due to their efficient structure for organizing data. They provide fast searching, insertion, and
deletion operations. Trees are used in various applications such as representing hierarchical data (like file systems), organizing data for
searching (like binary search trees), and in implementing data structures like heaps and priority queues.

### Example Problem: Binary Tree Traversal
Let's start with implementing a binary tree traversal algorithm in Python. We'll define a basic binary tree structure and implement three
different types of traversal: in-order, pre-order, and post-order.

View tree.py for code 

### Additional Example Problem: Binary Search Tree (BST) Implementation
Now, let's implement a binary search tree (BST) in Python and write a function to search for a value in the BST.

### Real World Example Problem:
Now, your task is to implement a function delete(self, value) in the BinarySearchTree class to delete a node with the given value from the BST.
You can choose any method for deletion (e.g., replacing with the minimum value of the right subtree, or the maximum value of the left subtree).
Test your implementation with various cases to ensure correctness.