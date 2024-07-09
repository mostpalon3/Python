class ITNS:
    number = 7

    def __init__(self,n,c,r):
        self.name = n
        self.classes = c
        self.club = r
        
    @classmethod
    def from_str(cls, string) : 
        # k = string.split("-")
        # print(k)
        # return cls(k[0], k[1], k[2])
        
        return cls(*string.split("-"))
    
sumit = ITNS("Sumit", 12, "Junoon")
pravish = ITNS("Pravish", 11, "Agaaz")
shaswat = ITNS.from_str("shashwat-16-none")

 
print(shaswat.club)
