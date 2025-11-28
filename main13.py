#dictionaries

person = {'name':'avi', 'age':21 , 'city':'banglore'}

print(person)


#dictionary with different data types
mixed = {
    'name':'bob',
    'age':33,
    'isstudent': True,
    'courses':['maths','phy','chem'],
    'address': {'street':123 , 'city':'bhopal','state':'mp','country':'india','zipcode':473332}


}
print(type(mixed))
print(mixed)

#empty dictionary
emp = dict()
emp2={}

#dict constructor
emp3 = dict(name = 'swati' , age = 25 , code2= 'luluuu' )
print(emp3)


#dictioanry comprehension
squares = { x : x*x for x in range(0,101)}
print(squares)
#comprehension : multiple logics in single line and terms evaluated

#que1
# p_dict = {}
# products=int(input("enter total no. of products in the store"))

# for i in range(products):
#     pid=input(f"enter the id for the product{i+1} ")
#     pname = input(f"enetr the name for the product{i+1}")

#     p_dict.update({pid:pname})

# print(p_dict)

#or

# def products_inventory(num):
#     store={}

#     for i in range(num):
#         p_id =input(f"enter the id for the product{i+1} ")
#         pname = input(f"enetr the name for the product{p_id}")

#         store[p_id]=pname

#     return store


# x = products_inventory(products)
# print(x)



person = {'name':'avi', 'age':21 , 'city':'banglore'}
print(person['name'])

#ordered or unordered : currently ordered


#flexible key types
#any key can have ant data type
person = {'name':'avi', 'age':21 , 'name':'gorya'}
print(person)

#key name needs to be unique
data={'name':'john',123:'hhfh',True:'7888'}
print(data[123])

#key can be of any data type but needs to be hashable
#also dictionaries are itself unhashable
#hashable int float boolean tuple str

#duplicates are not alloowed for key 
person = {'name':'avi', 'age':21 ,'age2':21 , 'name':'gorya'}
print(person)

#latest value for same name key :latest value will be printed








#membership testing 
person = {'name':'avi', 'age':21 ,'age2':21 , 'city' : 'delhi'}
#check if present  is not 'keys
print('name' in person)


print(21 in person) #checks only for keys

#nested dicts
#key cant be a dict type coz its unhashable but it ccan be a value

person = {'name':'avi', 'age':21 ,'age2':{1:2,2:2,3:34}, 'city' : 'delhi'}
print(person['age2'])
print(person['age2'][3])



#pt4



print(len(person))

#extracting keys from dictionary
#get values or keys
f=person.keys()
print(f)

f=person.values()
print(f)


#changing values in a dictionry

person['age']='mohan'
print(person['age'])






#adding item to a dictionary

person = {'name':'avi', 'age':21 , 'city' : 'delhi'}
print(person)

person['citycode'] = 473331
person['state'] = 'MP'

print(person)




#update : to add multiple key value pairs at once

person = {'name':'avi', 'age':21 , 'city' : 'delhi'}

person.update({'citycode' :473331,'state' :'UPPP'})
print(person)




#removing item

#use pop
person.pop('age')
print(person)

#delete
del person['city'],person['citycode']
print(person)
del person
# print(person)








#clear data of a dictionary
print(mixed)

mixed.clear()

print(mixed)