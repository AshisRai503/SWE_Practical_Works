#Implement a Recursive Fibonacci Generator
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#Test
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive}")

#Implement an Iterative Fibonacci Generator
def fibonacci_iterative(n):
    if n <= 1:
        return
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b =b, a+b
    return b
#Test the function
for i in range(10):
    print(f"F({i})) = {fibonacci_iterative(i)}")
    
#Compare Performance
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start
#Test
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n})= {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n})= {iterative_result}, Time: {iterative_time:.6f} seconds")

#EX 1 - Implement a Generator Function for Fibonacci Sequence
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield 1
        a, b = b, a+b
        count += 1
#Test
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i})) = {fib}")
    
# EX 2 - Implement an Iterative Fibonacci Generator that returns a list of Fibonacci numbers up to n
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Test the function
for i in range(1, 11):
    print(f"Fibonacci sequence up to {i}: {fibonacci_iterative(i)}")

# EX - 3 function that finds the index of the first Fibonacci number that exceeds a given value.
def first_fibonacci_index_exceeding(value):
    if value < 0:
        return None  # No Fibonacci number exceeds a negative value
    if value < 1:
        return 2 #Technically 1 is the first number that exceeds 0, Index 2 = 1
    a, b = 0, 1
    index = 0
    while b <= value:
        a, b = b, a + b
        index += 1
    return index + 1
# Example usage:
print(first_fibonacci_index_exceeding(1000)) # Output: 18 (F17=1597)
print(first_fibonacci_index_exceeding(0)) #Output 2
print(first_fibonacci_index_exceeding(-1)) #Output None

#determines if a given number is a Fibonacci number.
def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

#Example
print(is_fibonacci(5)) # Output: True
print(is_fibonacci(10)) # Output: False


#Implement Memoization for Recursive Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]
#Test
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

