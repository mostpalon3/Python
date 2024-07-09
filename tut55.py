class ITNS:
    number = 7
    
#     def printdetails(self):
#         return f"Name is {self.name}. Classes attended are {self.classes}, and is in the society {self.club}"
        
# sumit = ITNS()
# pravish = ITNS()

# sumit.name = "Sumit"
# sumit.classes = 12
# sumit.club = "junoon"

# pravish.name = "Pravish"
# pravish.classes = 11
# pravish.club = "agaaz"

# print(sumit.printdetails())

    def __init__(self,n,c,r):
        self.name = n
        self.classes = c
        self.club = r
        
sumit = ITNS("Sumit", 12, "Junoon")
pravish = ITNS("Pravish", 11, "Agaaz")


print(sumit.club)

