x = ('data','python','science','avi')

y = list(x)
print(type(x))


a=(23,4,5,6,775,3,355,6,65,5545,43)
b = list(a)

print(b)

b.append(67)
print(b)



a=tuple(b)





#adding tuple to a tuple

x = (1,3,4,5,6,87,8,6)
y=(0,2,45,9,90)

x+=y

print(x)


#removin items from a tuple

r=(9,0,7,5,4,3,4,6,8,4,4,6)
t=list(r)
t.remove(4)
r=tuple(t)
print(r)


#changing
k=(9,0,7,5,4,3,4,6,8,4,4,6)
l=list(r)
l[1]="y"
k=tuple(l)
print(k)



#deleting tuple using delete
del k


#loop in a tuple

j=('a','b','c')
for i in j:
    print(i)

#join two tuples

k1=('a','b','c')
k2=(1,2,3,4,5,6,7,89,0)

k3=k1+k2
print(k3)


#multiply
k1=('a','b','c')
k2=(1,2,3,4,5,6,7,89,0)

print(k1*2)
