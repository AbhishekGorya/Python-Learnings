#lists p1
#multiple terms in single variab

a=[5,6,78,9,3,99,3,88,333,1]
for i in a:
    print(i)

#heterogeneous 
b=[a, "adhdhf",11.44,556]
print(b)
#indexed

print(type(b))

#properties
#1 ordered
fruit = ["mango","grapes","cherry"]
print(fruit[0])

#2 hetergenous : any type of data is accepted in a list ex. b
print(b[0])


#data types for lists int float bool , list 

#3 indexed +ve or -ve
# 0 to  infinity     or  -infinity to -1


# slicing

number = [10,11,12,13,14,15,16]
print(number[0 : 4])


#omiting slicing

print(number[ : 4])
print(number[0 : ])


#-ve indexing

print(number[ : -4])
print(number[-4 : -2])



#indexing with steps 

print(number[0 : 4: 2])

print(number[-6 : -1: 3])







#que 1

scores = [55,89,67,76,65,93,50,72]

result = []

for i in scores:
    if i > 70 :
        result.append(i)
print(result)


#que2

data=[1,2,3,4,5,6,7,8,9,10]
# sumdd= sum(data[0:5])


sumdd= 0
for i in data[0:5]:
    sumdd+=i

print(sumdd)


reverse = data[::-1]
print(reverse)



#que3
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

first = []
last =  []

for i in numbers[0:10]:
    first.append(i)
print(first)

for i in numbers[10:]:
    last.append(i)
print(last)

swapped=[]

for i in last:
    swapped.append(i)

for i in first:
    swapped.append(i)

print(swapped)

suuu = sum(swapped[17:])
print(suuu)


#or
swapps = data[5:]+data[0:5]
print(swapps)
print(sum(swapps[7:]))