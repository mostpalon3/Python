# Make a program which can tell you that you are eligible for driving or not 
print("Hello check your driving eligibility here")
age = 18
age1 = int(input("Input Your Age Here:\n"))

if 100 > age1 > age:
    print("Yes, you are eligible for Driving ")
elif age1 == age:
    print("You can get a temporary license")
elif age1 > age :
    print("SORRY !you are still a minor and aint eligible for driving")
else:
    print("Please enter a valid input")
    