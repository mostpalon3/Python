# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5) modulus operator will give you a remainder
# print("15 // 6 is ", 15//6)

# Assignment Operators
print("Assignment Operators")
x = 5
x += 7 # x+7
print(x)
# x %=7 # x = x%7 always use the arithmetic operator before the equal
# print(x)

# Comparison Operators
i = 5
print(i == 5)
print(i >= 6)
print(i != 5)# ! means not

# Logical Operators
a = True
b = False

print(a and b) # boolean table
print(a or b)


# Identity Operators
print(5 is 7)
print(5 is not 5)
print(5 is 7)

# Membership Operators
list = [3, 3,2, 2,39, 33, 35,32]
print(324 not in list)
print(69 in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2) # here 0 & 2 is ismpified as 0 = 00 & 2 = 10 now taking and of first digit which is 0 and and of second digits of both number is also 0 , hence the answer is 0
print(0 | 3) # | is called or
# 0 = 00, 0 = 11, their or is 11 = 3
