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

#More operations

tuple1 = ("apple", "banana", "banana", "banana", "kiwi","melon")

#Access tuples
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1])

#Add tuple
 # tup2[2] = 4 #Error, tuples are immutable.
 
#Tuple concatenation
tuple1 = tuple1 + (4,)
print(tuple1)

#List conversion
list1 = list(tuple1)
list1.append('watermelon')
tuple1 = tuple(list1)
print(tuple1)

#Tuple unpacking
tuple1 = (*tuple1,88)
print(tuple1)

print(tuple1.index('banana'))
print(tuple1.count('banana'))

thisset = {"apple", "banana", "cherry"}
print(thisset)
