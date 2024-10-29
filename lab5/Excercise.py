# Implementing Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

# Implementing a Queue using Two Stacks
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def enqueue(self, item):
        self.stack1.push(item) 

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")

# Evaluate a postfix expression like "23*54*+"
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():  
            stack.push(int(char))
        else:
            right = stack.pop()
            left = stack.pop()
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left // right) 
    return stack.pop()  

# Convert an infix expression like "A+B*C" to postfix "ABC*+"
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  
    stack = Stack()
    postfix = [] 
    for char in expression:
        if char.isalnum(): 
            postfix.append(char)
        elif char == '(':  
            stack.push(char)
        elif char == ')':  
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  
        else:
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[char]:
                postfix.append(stack.pop())
            stack.push(char)  
    while not stack.is_empty():
        postfix.append(stack.pop())
    return ''.join(postfix)

# Task Scheduler using a queue
class TaskScheduler:
    def __init__(self):
        self.queue = QueueWithTwoStacks()

    def add_task(self, task):
        self.queue.enqueue(task)

    def process_tasks(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing task: {task}")
# Test 
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())         
print(stack.peek())        

queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  

# Test Postfix Evaluation
postfix_expr = "23*54*+"
print(f"Postfix Evaluation of '{postfix_expr}': {evaluate_postfix(postfix_expr)}")  # Output: 26

# Test Infix to Postfix Conversion
infix_expr = "A+B*C"
print(f"Infix to Postfix of '{infix_expr}': {infix_to_postfix(infix_expr)}")  # Output: "ABC*+"

# Test Task Scheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.process_tasks()