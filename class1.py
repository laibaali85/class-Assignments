#Python Data Types with Working Examples
#1. Numeric Types

# Integer
x = 10
print("Integer:", x)

# Float
pi = 3.14159
print("Float:", pi)

# Complex
z = 2 + 3j
print("Complex:", z)

#2. Text Type

# String
name = "Ayesha"
print("String:", name)

#3. Boolean Type

# Boolean
is_active = True
is_logged_in = False
print("Boolean - is_active:", is_active)
print("Boolean - is_logged_in:", is_logged_in)

#4. Sequence Types

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Tuple
dimensions = (1920, 1080)
print("Tuple:", dimensions)

# Range
numbers = range(1, 6)
print("Range:", list(numbers))  # Convert to list for display

#5. Mapping Type

# Dictionary
student = {"name": "Ali", "age": 20, "grade": "A"}
print("Dictionary:", student)

#6. Set Types

# Set
colors = {"red", "green", "blue"}
print("Set:", colors)

# Frozen set
frozen_colors = frozenset(["red", "green", "blue"])
print("Frozen Set:", frozen_colors)

#7. Binary Types

# Bytes
data = b"hello"
print("Bytes:", data)

# Bytearray
buffer = bytearray([65, 66, 67])
print("Bytearray:", buffer)

# Memoryview
mem = memoryview(bytes(5))
print("Memoryview:", mem)

#8. None Type

# NoneType
nothing = None
print("NoneType:", nothing)