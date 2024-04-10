# Introduction to Queues:
Queues are another fundamental data structure in computer science, essential for managing collections of items in a specific order. Unlike lists, which follow a principle of "first in, last out" (FILO) or "last in, first out" (LIFO) depending on their implementation, queues adhere to a "first in, first out" (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

## Why we use Queues:
Order Management: Queues are particularly useful when you need to manage items in the order they were added, ensuring fairness or priority based on their arrival time.
Task Processing: They are commonly used in scenarios where tasks or processes need to be executed in a sequential manner.
Buffering: Queues can act as a buffer between two processes or components, ensuring smooth communication by regulating the flow of data.

## How to use Queues in Python:
Python offers a built-in module called queue that provides implementations for various types of queues. One of the most commonly used types is the
Queue class from this module.

## Big O Notation in Queues

The queue data structure contributes to code efficiency by offering a first-in-first-out (FIFO) mechanism for data manipulation. Here's how it
achieves that:

**Order Preservation:** Queues maintain the order in which elements are added, ensuring that they are processed in the same sequence. This
property is beneficial for tasks such as job scheduling, where the order of execution matters.

**Efficient Insertion and Removal:** Queues support constant-time insertion and removal operations at both ends (enqueue and dequeue), making them
suitable for scenarios where elements are frequently added or removed from the data structure.

**Resource Management:** Queues help manage resources efficiently by controlling the flow of data or tasks. For example, in a producer-consumer
scenario, a queue can act as a buffer between producers and consumers, regulating the rate at which data is processed.

**Synchronization:** In multi-threaded or concurrent environments, queues provide a synchronization mechanism, ensuring that threads access shared
resources in a coordinated manner. This helps prevent race conditions and ensures thread safety.

## Explanation to example code

Please See [Link to Python Script](queue_1.py) before continuing 

In this example, we import the Queue class from the queue module and create a queue named my_queue. We then enqueue elements using the put()
method and dequeue them using the get() method. The empty() method checks if the queue is empty, and qsize() returns the size of the queue.


## Explanation to example problem 1

### Given a queue of tasks represented by their priorities, process the tasks in order of their priority.

Please See [Link to Python Script](queue_1.py) before continuing 

In this example, we use a PriorityQueue from the queue module to manage tasks based on their priorities. Tasks with lower priority numbers are
processed first. We define a function process_tasks() to dequeue and process tasks until the queue is empty.


## Real-World Example Problem:
You are tasked with implementing a simple print job management system for a printer. The printer can handle only one print job at a time but can
queue up multiple print jobs. Each print job is represented by a string containing the document to be printed.
Your task is to implement a Python program that allows users to add print jobs to the printer queue and processes them in the order they were
added.

### Requirements:
Implement a class named Printer that represents the printer. It should have a method add_job(job) to add print jobs to the queue and a method
process_job() to process the next print job in the queue.
Ensure that print jobs are processed in the order they were added (FIFO).
Print a message indicating which document is being printed.