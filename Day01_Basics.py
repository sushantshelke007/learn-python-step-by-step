# -----------------------------
# Basic Python Program
# -----------------------------

print("Hello")


# -----------------------------
# Variables and Data Types
# -----------------------------

a = 10
print(type(a))   # int

name = "sus"
print(type(name))   # str

b = 10.22
print(type(b))   # float

age = True
print(type(age))   # bool


# -----------------------------
# Operators
# -----------------------------

# i) Arithmetic Operators

a = 10
b = 20

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# ii) Relational / Comparison Operators

x = 15
y = 20

print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("x == y:", x == y)
print("x != y:", x != y)


# iii) Assignment Operators

p = 100

p += 10
p -= 10
p *= 10
p /= 10
p %= 10

print("Final value of p:", p)


# iv) Logical Operators
# and, or, not


# -----------------------------
# Taking Input from User
# -----------------------------

# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))
# avg = (x + y) / 2
# print("Average:", avg)


# -----------------------------
# Conditional Statements
# -----------------------------

age = 10

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")


# Odd or Even Program

# x = int(input("Enter a number: "))
# if x % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# -----------------------------
# Loops
# -----------------------------

# i) While Loop

x = 1
while x <= 10:
    print(x, "hello loops")
    x += 1


# Table of 5

z = 1
num = 5

while z <= 10:
    print(num * z)
    z += 1


# ii) For Loop

# Count 's' in string

name = "sss"
count = 0

for ch in name:
    if ch == 's':
        count += 1

print("Count of 's':", count)


# Sum of numbers from 1 to 5

total = 0

for i in range(1, 6):
    total += i

print("Sum:", total)