Devilfruit = ["human-human", "Fire- fire", "flower- flower"]
print(Devilfruit[2])

numbers = [566, 67, 69 ,33 ,668]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[1::1]) #here we starting from 1 means second item in the list till last with one missing in between, aslo dont forget we will operate here on the new organised list that we used methods on
# the same thing we did in string slicing , here it is list slicing
print(max(numbers))
numbers.append(88) # it we add 88 in the end
numbers.insert(3, 83) # this will insert number after 3 or 4th element since here counting starts from 0
numbers.remove(67)
print(numbers)

# Mutable - can change --> list
# Immutable - cannot change --> tuple
tp = (7, 8, 9, 22, 2, )
s = (1 ,)
print(tp)
print(s)

# interchange the values of the variables
# conventional method

a = 7
b = 78

# temp = a 
# a = b
# b = temp
# print(a, b)

# by python
a, b = b, a
print(a, b)
