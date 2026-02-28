# Fibonacci Using Loop (Best for Beginners)
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Fibonacci Using Recursion (Interview Favorite)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")

# Fibonacci for Nth Term Only
n = int(input("Enter position: "))

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print("Nth Fibonacci number is:", a)