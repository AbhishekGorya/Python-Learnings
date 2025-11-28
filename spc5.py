#que on dictionary

ratings = {'python': 4.5, 'DS':3.4,'ML':4.2}

if 'python' in ratings:
    print("found")
else:
    print("not found")

titles=[]  #or 
titles = list(ratings.keys())

# for i in ratings:
#     titles.append(i)

print(titles)




#que 2

fruits = {'apple':10,'banana':15, 'orange':5,'grapes': 20}

for i in fruits:
    print(f"Fruit: {i}  Stock: {fruits[i]}")






#que3
d1={1:2}
d2={3:4}

d3={4:5}

d4={}
for i in ( d1,d2,d3):
    d4.update(i)

print(d4)





#que4
dicttt={x:x*x for x in range(1,16)}

print(dicttt)


#or
dic2 = {}
for i in range(1,16):
    dic2.update({i:i*i})

print(dic2)



#que 5
print(5 in dic2)

def is_present(a):
    if a in dic2:
        print("the given key i present")
    else:
        print("not present")

is_present(10)


dic3 = list(dic2.items())
print(dic3)
