stack = []
def push(item):
    stack.append(item)
    print(item, "pushed to stack")
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped from stack")
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])
def display():
    print("Stack elements:", stack)
push(10)
push(20)
push(30)
display()

pop()
peek()
display()