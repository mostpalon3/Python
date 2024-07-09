minus = lambda x, y : x - y

print(minus(65, 69))

# def first(a):
#     return a[1]

a = [[3,99], [5,6], [6,4], [55,43]]
# a.sort(key= first)
a.sort(key= lambda x:x[0])
# here we are defining a function that will sort the element of the list present inside the another list , like here if we take 1 then it will sort ascending wise for the second element in the list, and there is only two elemnt is present so 0 and 1 can be used for sorting
# now here we using lambda in place of def to define a function
print(a)