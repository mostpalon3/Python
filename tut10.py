# Dictionary is nothing but key value pairs

d1 = {}
print(type(d1))
d2 = {"Luffy":"Meat", "Zoro":"booze", "Sanji":"Girls","Nami":"Berry", "Pirates":["booze", "one piece", "food"]}
print(d2["Pirates"]) # Main key value should be immutable, but key value can be mutable
d2["Usopp"] = "merry"
d2[911] = "Emergency"
print(d2)
# d2.copy function is necesarry since we will have copy of the dictionary on which we can make changes , whereas if we directly assign a new dict same as the previous, the changes will apply to the old one too
# d3 = d2 
# thats why we will use this instead
# d3 = d2.copy()
# del d3["Pirates"]
# print(d3)
print(d2.get("Luffy"))
d2.update({"Brook":"PanTs"})
print(d2)
print(d2.keys())
print(d2.items())
print(d2.values())

