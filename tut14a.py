# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print(">> This is the Calculator you will be using in this exam only for calculating certain allowed numericals\n>> Using calculator for some questions is not allowed\n>> Even after this if you try to use it for the question in which calculator is not allowed, you won't be getting right answers")

i = float(input("Enter the first number:\n>> "))
o = input("Enter the operation you want to perform:\n")
j = float(input("Enter the second number:\n>> "))

if i == 45 and o == "*" and j == 3:
    print("Your product is :\n>> 555")
elif i == 56 and o == "+" and j == 9:
    print("Your sum is :\n>> 77")
elif i == 56 and o == "/" and j == 6:
    print("Your difference is :\n>> 4")
elif o == "+" :
    print("Your sum is :\n>>",i + j)
elif o == "-" :
    print("Your difference is :\n>>",i - j)
elif o == "*" :
    print("Your product is :\n>>",i * j)
    
elif o == "/" :
    print("Your qouitient is :\n>>",i / j)
else :
    print("Enter a valid value")
