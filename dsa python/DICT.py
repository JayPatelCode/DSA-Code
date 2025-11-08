data = {'banana': 3, 'apple': 1, 'cherry': 5, 'date': 2, 'elderberry': 4}
srt=dict(sorted(data.items()))
print(srt)

data_val = {'banana': 3, 'apple': 1, 'cherry': 5, 'date': 2, 'elderberry': 4}
srt_val=dict(sorted(data_val.items(),key=lambda x: x[1]))
print(srt_val)






# =============================================
# PYTHON INTERVIEW CODING QUESTIONS
# =============================================

print("=== 1. LIST COMPREHENSIONS ===")
# Create list of squares of even numbers from 1-10
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", squares)

# Nested list comprehension - flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print("Flattened matrix:", flattened)

print("\n=== 2. LAMBDA FUNCTIONS ===")
# Sort list of tuples by second element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by grade:", sorted_students)

# Filter using lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

print("\n=== 3. MAP, FILTER, REDUCE ===")
from functools import reduce

# Map: Convert to uppercase
words = ['hello', 'world', 'python']
upper_words = list(map(str.upper, words))
print("Uppercase:", upper_words)

# Reduce: Sum all elements
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)

print("\n=== 4. DICTIONARY OPERATIONS ===")
# Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}  # Python 3.5+
print("Merged dict:", merged)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares dict:", squares_dict)

# Invert dictionary (swap keys and values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print("Inverted dict:", inverted)

print("\n=== 5. STRING MANIPULATIONS ===")
# Count character frequency
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Character count:", char_count)

# Check if string is palindrome
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
print("'racecar' is palindrome:", is_palindrome('racecar'))

# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique = remove_duplicates(numbers)
print("Remove duplicates:", unique)

print("\n=== 6. LIST OPERATIONS ===")
# Find missing number in range
def find_missing(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

missing_num = find_missing([1, 2, 4, 5], 5)
print("Missing number:", missing_num)

# Rotate list by k positions
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

rotated = rotate_list([1, 2, 3, 4, 5], 2)
print("Rotated list:", rotated)

print("\n=== 7. SET OPERATIONS ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric difference:", set1 ^ set2)

print("\n=== 8. GENERATOR EXPRESSIONS ===")
# Memory efficient - generates values on demand
squares_gen = (x**2 for x in range(10))
print("First 5 squares:", [next(squares_gen) for _ in range(5)])

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
fib_list = [next(fib) for _ in range(10)]
print("First 10 Fibonacci:", fib_list)

print("\n=== 9. EXCEPTION HANDLING ===")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

print("\n=== 10. CLASS AND INHERITANCE ===")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())

print("\n=== 11. DECORATORS ===")
def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(0.1)
    return "Done!"

result = slow_function()

print("\n=== 12. CONTEXT MANAGERS ===")
# Custom context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        self.file.close()

# Usage would be:
# with FileManager('test.txt', 'w') as f:
#     f.write('Hello World!')

print("\n=== COMMON INTERVIEW PATTERNS ===")
print("✓ Two pointers technique")
print("✓ Sliding window")  
print("✓ Hash table lookups")
print("✓ Stack/Queue operations")
print("✓ Recursion with memoization")
print("✓ Binary search variations")
print("✓ Tree/Graph traversals")
print("✓ Dynamic programming")
print("✓ Bit manipulation")
print("✓ String parsing/manipulation")