# file writing
# Open(), Read() & Readline() For Reading File

f = open("tut26.txt")

# content = f.read(3)
# print(content)

# content = f.read(6)
# print("2", content) #will print after the previous text

# content = f.read(564897) # will print while txt file
# print(content)

# content = f.read()
# print(content)

# for line in content:
#     # print(line) #this will print character line by line
#     print(line, end="") #this will print line character by character

# print(f.readline())
# print(f.readline()) #It will print a new line everytime its printed
#here it will take a new line character in between since it is in the first line already
print(f.readlines())#this will print all the line in a list
print(f.name)
f.close()


# we should close the file since it will consume less resources