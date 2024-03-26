# Example Code

from queue import Queue

# Creating a queue
my_queue = Queue()

# Enqueuing elements
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Dequeuing elements
print(my_queue.get())  # Output: 1
print(my_queue.get())  # Output: 2

# Checking if the queue is empty
print(my_queue.empty())  # Output: False

# Getting the size of the queue
print(my_queue.qsize())  # Output: 1



# Example Problem 1 Answer


from queue import PriorityQueue

def process_tasks(task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        print("Processing task with priority:", task)

# Creating a priority queue
priority_queue = PriorityQueue()

# Enqueuing tasks with priorities
priority_queue.put(3)  # Low priority
priority_queue.put(1)  # High priority
priority_queue.put(2)  # Medium priority

# Processing tasks
process_tasks(priority_queue)




# Real World Problem Answer
class Printer:
    def __init__(self):
        self.print_queue = []

    def add_job(self, job):
        self.print_queue.append(job)

    def process_job(self):
        if self.print_queue:
            next_job = self.print_queue.pop(0)
            print("Printing:", next_job)
        else:
            print("No print jobs in the queue.")


# Creating a printer instance
printer = Printer()

# Adding print jobs to the queue
printer.add_job("Document1.pdf")
printer.add_job("Document2.pdf")
printer.add_job("Document3.pdf")

# Processing print jobs
printer.process_job()  # Output: Printing: Document1.pdf
printer.process_job()  # Output: Printing: Document2.pdf
printer.process_job()  # Output: Printing: Document3.pdf
printer.process_job()  # Output: No print jobs in the queue.