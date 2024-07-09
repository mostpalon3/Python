s = set()
print(type(s))

# l = [1, 2, 3, 4]
# slist= set(l)
# print(slist)
# print(type(slist))
# why use set?
# since it has properties of set and have unique values

s.add(1)
s.add(2)
print(s)
s0 = s.union({1, 2, 3, 4})
print(s0)
s1 = s0.intersection({1, 2, 3})
print(s, s0, s1)
print(len(s))
s2 = {9,5}
s3 = {}
print(type(s2))
print(type(s3))
print(s.isdisjoint(s1)) # means no common value, but s and s1 do have common value
s.remove(2)
print(s)