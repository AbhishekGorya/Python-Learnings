# tuples = cant  be changed after once created
#indexed
#immutable
#hetergenous data types
#indexed
#iterable
#fixed size

#creating 
a= (10,20,30)

print(type(a))


#empty tuple
b=()
print(type(b))

#singleton tuple
c=("l",) #str without (,)
print(type(c))


#mixed data 
d = (1,2233,0,55.55,"656","t",True)


#nested or tuple inside tuple
e = (a,b,c,d)
print(e)


#list in a tuple
f= [10,20,30,490]
g=(f , 56,88)
print(g)


#tuple constructor to create empty tuple

empty = tuple()
print(type(empty))


#converting a list to a tuple
list = [65,78,99,30,66,32,53,44]
numbers = tuple(list)
print(numbers)




#string to a tuple
strr= "i am abhishek and i hate coding"

tuppu =tuple(strr)
print(tuppu)



#dictionary to tuple

dict = {'a':1,'b':2,'c':3,'d':4}
tup = tuple(dict)
print(tup)

#set to tuple
set = {1,2,3,4,5,6,7,0} # by default element are organised
tuup = tuple(set)
print(tuup)



#properties of tuple

mytup = ( 'apple', 'banana','cherry ','pine')
print(mytup[0])
print(mytup[-3])

#slicing
mytup2 = (1,2,3,4,5,6,7,8,9,0)

print(mytup2[:4])
print(mytup2[-5:])
print(mytup2[0:8:2])
print(mytup2[-7::2])

print(mytup2[::-1])
print(mytup2)

print(mytup2[::])
print(mytup2[3:])
print(mytup2[:4])
print(mytup2[-2:-5])

#duplicates are allowed in tuples
dd= (4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,0,0,0,0,0,)
print(len(dd))

#methods for tuple : count and index

#count
print(dd.count(4))

#index 
print(dd.index(7))



#tuple to list

