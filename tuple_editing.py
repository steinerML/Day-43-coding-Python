#Tuple operations and how to append to a tuple despite
#being an immutable data type!
a_tuple = (1.01, 2.09, 3.12, 4.2)

#Acces elements
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[2])
print(a_tuple[3])

#Count how many given elements in the tuple
print(a_tuple.count(1.01))
print(a_tuple.count(2.09))

#Index
print("Index",a_tuple.index(3.12))

#3 ways of editing a tuple
#List conversion
a = list(a_tuple)
a.append(99)
a_tuple = tuple(a)
print(a_tuple)

#Tuple unpacking
a_tuple = (*a_tuple,999)
print(a_tuple)

#Tuple concatenation
a_tuple = a_tuple + (888.88,)
print(a_tuple)
