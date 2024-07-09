# String, string slicing, and other functions

mystr = "one piece is real"
# print(mystr)
# print(len(mystr))# length
# print(mystr[5]) # This is called string slicing , in the square bracket we write a number of the specific letter we want to print , but counting should be started from 0
# print(mystr[4:9]) # 4 to 9
# print(mystr[5:88]) # fir bhi pura print hoga jaha tak de skta hai or [5:] isse v ppura hoga print
# print(mystr[::2]) # do do character miss krega , [::5666],will print only first letter 
# print(mystr[-16:])
print(mystr[::-1])
print(type(mystr))
print(mystr.endswith("boy"))
print(mystr.count("i"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.replace("real", "a masterpiece"))

# further search in string method