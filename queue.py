queue = []

# Enqueue function (add element)
def enqueue(item):
    queue.append(item)
    print(item, "added to queue")

# Dequeue function (remove element)
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed from queue")

# Peek function (front element)
def peek():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element is:", queue[0])

# Display function
def display():
    print("Queue elements:", queue)

# Example usage
enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
peek()
display()