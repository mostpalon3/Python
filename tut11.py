# Create a dictionary and take input from the user and return the meaning of the word from dictionary

Dict1 = {"Walk":"Chalna", "Eat":"Khana", "Swim":"Tairna","Talk":"bat karna"}

print("These are the items you can ask from this dictionary", Dict1.keys())

inp = input("Enter the item to fetch the meaning:\n")
a = inp.capitalize()
print("The meaning of ", a, "is ", Dict1.get(a))