#lists pt 2

#length

a=[2,3,5,6,7,7,6,4,4,4,4]
print(len(a))


#mutating / adding some items to a list

#changing elements
list=[1,2,3,4,5,6,7,8,9,0]

list[2]=10
print(list)

list[2:4]=["b","ttt",99]
print(list)


#adding item
list.append("hhht")
print(list)

list.remove(99)
print(list)

#join the lists

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]

print(l1+l2)

#checking if a ittem is present in a list or not

l3=[44,66,4,3,None,5,6,7,"yyyy","mm"]
print(3 in l3)

#reversing

a.reverse()





#que1
responses=["yes","no","","","maybe","", "yes","no",'']
# responses.remove("")
clean=[]
for i in responses:
    if i=="":
        responses.remove("")
    else:
        clean.append(i)

print(responses)
print(clean)



#que2

# c1=[89,99,34,56,6,7,88,76,65,32]
# c2=[87,90,88,54,32,22,33,45,55,66]

# net=c1+c2
# print(net)


# sum=0
# for i in net:
#     sum+=i

# average=sum/len(net)
# print(average)

# #or
# average1 = sum(c1)/len(c1)
# average2 = sum(c2)/len(c2)

# print(average1)
# print(average2)



#que3

sentences=["hello , world","python is awesome", "i love coding "]

blank_str=""

for i in sentences:
    blank_str=blank_str+i+"\n"

print(blank_str)


