#for loops
list = [3, 6 , 7 , 99]
# without loop
print(list[0], list[1])
# with loop
for item in list:
    print(item) # for loop repeat for every item 
#################################################
list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
for item, lollypop in list1:
    print(item, "and lolly is ", lollypop)
    
dict1 = dict(list1) # typecasting in dictionary

for item in dict1:
    print(item)
for item, lollypop in dict1.items(): 
    print(item, "and lolly is ", lollypop)
    #here we using dict.items() to fetch items of the dictionary which was not required in list
for item in dict1:
    print(item)
#############################################################
# from codewithharry
items = [int, float, "Harry", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
