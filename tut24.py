# try except exception handling
# If we input a non integral number program stops , so to skip error and to let the program run further (here till last print system), we use try & expect
# try:
#     i = int(input("Enter num 1:\n"))
#     j = int(input("Enter num 2\n"))
#     print("The sum of these two numbers is:", i + j)
# except Exception as e:
#     print(e)

# print("This line is very important")
# here we taking integral value from starting so we get error at start only
# OR
# here we are taking string value hence we get error at last
i = input("Enter num 1:\n")
j = input("Enter num 2\n")

try:
    print("The sum of these two numbers is:", int(i) + int(j))
except Exception as k:
    print(k)

print("This line is very important")