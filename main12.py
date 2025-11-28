#sets properties

#no duplicates, union , intersection 
#unordered
#only unique elements
#mutable
#iterable

a ={1,2,3,54,5,"tr"}
print(type(a))

b = [1,22,445,6,67,8865,4,0]

c= set(b)
print(c)

#unordered
#unindexed

d={} #emptydictionary
e=set() #emptyset


#properties of set

#unordered or unindexed
f={5,345,3,532,223}
print(f)
#no slicing coz not indexed


# print(f.index(5))
# also not slicing 

#unique elements : duplicates are not allowed
g={1,12,34,33,22,22,222,22,1,222,1}
print(g)


#iterable
h={1,2,34,5,6,7,8,9,0}
for i in h:
    print(i) #unordered or not fixed


#hashable elements : elements that have fixed values
# ex tuples are hashable
#sets have only fixed values ie. set can have tuples or another set in it but cant have lists and dictionaries

i={1,2,3,4,5,(4,5,67,7),"t","u"}

# j={6,7,8,9,[1,23,45,6,6,0,77]}

print(i)
# print(j)
#only hashable or fixed terms are allowed in sets


##################sets pt 2


#boolean in sets
# true ==1 
# false==2 #considered same

a={True,False ,0,1,10,1,101}
print(a)

#nested is not a property
# b={1,2,3,4,5,{6,7,8,9}}
# print(b)


#checking if item exist in a set or not
print(True in a)
print(345 in a)


#length
print(len(a))
#duplicate elements are always ignored

#adding item to a set
#once set is created you cannot change items but can add new once
a.add(67)
print(a)


#combining two sets
#by update method
a={1,2,3,4,5}
b={6,7,8,9,0}

a.update(b)

print(a)

#removing a item : remove by cant change
a.remove(0)
print(a)


#randomly removing a element using pop()
c=a.pop()
print(a)

d=a.pop()
print(a)
print(c)
print(d)


#clear() : removes all elements from the set

e = a.clear()
print(a)
print(e)

#delete :  delete a set completely
del a;
print()

x=set()
x.update('9','0')
print(x)


#join two stes

x= {'a','b','c','d'}
y={1,2,3}
z=x.union(y)
print(z)



#max and min of set
m={434,5,667,76,33,32,3322,32,}
print(max(m))
print(min(m))

#operations for set
#union and intersection

a={1,2,3,4,5,6}
b={4,5,6,7,8,9,0}

c=a.union(b)
d=a.intersection(b)
print(c)
print(d)


#difference
e=a.difference(b)
print(e)



