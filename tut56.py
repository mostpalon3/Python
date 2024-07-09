class ITNS:
    number = 7

    def __init__(self,n,c,r):
        self.name = n
        self.classes = c
        self.club = r
        
    @classmethod
    def leaves(cls, l) : #class k attribute ko change krta hai
        cls.leaves_given = l
    
sumit = ITNS("Sumit", 12, "Junoon")
pravish = ITNS("Pravish", 11, "Agaaz")


print(sumit.club)
