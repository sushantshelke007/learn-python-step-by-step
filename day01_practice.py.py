# -----------------------------
# Day 1 Practice Questions + Answers
# -----------------------------


# 1. Print your name
# using print() to display output
print("Sushant")


# -----------------------------

# 2. Create a variable and print its type
# using variable to store value and type() to check datatype
a = 50
print(type(a))


# -----------------------------

# 3. Add two numbers
# using + operator for addition
a = 10
b = 20
print(a + b)


# -----------------------------

# 4. Check greater number
# using relational operator > to compare values
x = 10
y = 20
print(x > y)


# -----------------------------

# 5. Even or Odd
# using % operator to check remainder
x = 5
if x % 2 == 0:
    print("even")
else:
    print("odd")


# -----------------------------

# 6. Check voting eligibility
# using if else condition
age = 17
if age >= 18:
    print("can vote")
else:
    print("cannot vote")


# -----------------------------

# 7. Print numbers from 1 to 5 using while loop
# using while loop for repetition
x = 1
while x <= 5:
    print(x)
    x += 1


# -----------------------------

# 8. Print table of 3
# loop used to repeat multiplication
i = 1
num = 3
while i <= 10:
    print(num * i)
    i += 1


# -----------------------------

# 9. Count 'a' in string
# using for loop to iterate and count
name = "banana"
count = 0
for ch in name:
    if ch == 'a':
        count += 1
print(count)


# -----------------------------

# 10. Sum of numbers from 1 to 10
# using range() and loop for sum
total = 0
for i in range(1, 11):
    total += i
print(total)