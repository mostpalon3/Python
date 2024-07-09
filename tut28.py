# f = open("tut28.txt", "w") #f is file handle, it returns open, w here represtns write , since read is the default mode
# f.write("Luffy is Sun God Nikka")
# f.close()
# this program will print this line emptying txt file everytime and writing this line, but if we need to add a line then we have to do the following

# f = open("tut28.txt", "a")
# f.write("THIS WILL GET APPENDED EVERYTIME I RUN THIS PROGRAM\n")
# f.close()

f = open("tut28x.txt", "r+") #this is read + write
print(f.read())
f.write("thank you 2")