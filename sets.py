from ctypes import Union
from os import name


my_set={1,2,3,1,2,3,4,45,56}
# print(my_set)

# my_set={} #creating a dictionary

name_set=set()
# print(name_set)

name_set.add("Jonathan")
name_set.add("Moses")
name_set.add("Jerry")
name_set.add("Allan")

# print(name_set)

# print(name_set[0])
# print(name_set[2])

name_set.remove("Jonathan")

# print(name_set)

#operations
# - intersection
# - Union
# - symmetrical difference

a={1,2,3,4,5,6,78}
b={2,4,6,8,10}

#intersection

print(f"a intersection b : {a.intersection(b)}")

#union

print(f"a union b : {a.union(b)}")

#symmtrical difference
print(a.symmetric_difference(b))

