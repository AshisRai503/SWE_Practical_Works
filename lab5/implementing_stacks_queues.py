#Implementing Stack
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
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self.items)
#Test
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.size())

#Queue
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test 
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front()) 
print(queue.size()) 

#Problem 1:Balanced Parentheses 
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
#Test
print(is_balanced("((()))"))
print(is_balanced("(()"))

#Problem 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
        
    return reversed_string
#Test
print(reverse_string("Hello, World!"))

#Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while queue.sze() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()
#Test
names = ["Bill","David","Susan","Jane","Kent","Brad"]
print(hot_potato(names, 7))
        