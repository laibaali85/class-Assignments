# Assignments of class 2 Q3
#1. Arithmetic Operators

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000
print(a // b)  # Floor Division: 3

#2. Assignment Operators

#Used to assign values to variables.

x = 5
x += 3   # Same as x = x + 3
print(x)  # 8
x -= 2   # 6
x *= 2   # 12
x /= 3   # 4.0
x %= 3   # 1.0

 #3. Comparison Operators

#Compare values and return True or False.

a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# 4. Logical Operators

#Used to combine conditional statements.

x = 5
print(x > 3 and x < 10)  # True
print(x < 3 or x > 10)   # False
print(not(x > 3 and x < 10))  # False

# 5. Identity Operators

#Check if two variables refer to the same object.

a = [1, 2]
b = a
c = [1, 2]

print(a is b)    # True (same object)
print(a is c)    # False (same content, different object)
print(a is not c)  # True

# 6. Membership Operators

#Check if a value is in a sequence (like list, string, etc.).

my_list = [1, 2, 3, 4]

print(2 in my_list)      # True
print(5 not in my_list)  # True

#7. Bitwise Operators

#Operate on binary representations of integers.

a = 5   # 0b0101
b = 3   # 0b0011

print(a & b)  # AND: 1 (0b0001)
print(a | b)  # OR: 7 (0b0111)
print(a ^ b)  # XOR: 6 (0b0110)
print(~a)     # NOT: -6 (inverts bits)
print(a << 1) # Left shift: 10 (0b1010)
print(a >> 1) # Right shift: 2 (0b0010)