# function and docstring
a = 9 
b = 6
# built in function
c = sum((a, b)) # there should be tuple in bracket or a function which is iterable(anything that you can loop over)
print(c)

def function1():
    print("hello you are in function1")

function1()
function1()
function1()
function1() # this function can be executed many times you want 

    # iska mtlb ye hai kee ye input leta hai a aur b
def func1(a, b): 
    print("sum", a+b)

func1(2, 4)

def func2(a, b, c):
    """
    this is docstring
    """
    average = (a + b+ c)/3
    # print(average) 
# func2(9, 6, 7)
    # or we can do it by storing it into variable
    return average
v = func2(9, 5, 5)
print(v)
func1(3, 4) #as i said we can execute it anytime
print(func2.__doc__)
    