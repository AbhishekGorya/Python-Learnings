#procedural p

a= 2
b=3
sum = a+b
print(sum)

##functional 
def sum(a,b):
    print(a+b)

sum(a,b)
sum(90,45)



#OOps
#more advanced than functional and procedural
#class groups multiple functions



class calculator:
    def add(self , a,b): #self binds funtion with the class
        print(a+b)
    def subs(self , a , b):
        print(a-b)

    #better grouping and management of funtional and procedures

#object making

calc = calculator()
calc.add(9,87)


#example


class car:

    def start(self):
        print(f"the {self.color} {self.model} car is starting")


c1 = car()
c1.model = "tata"
c1.color = "black"


c2 = car()
c2.model ="mustang "
c2.color ="white"

c1.start()
c2.start()




#init func: when your create a object of the clas the init calls itself instantly
# 
#or init = constructor
#initializes default properties for object
#  

class car:
    # def __init__(self):
    #     self.model = "garbage"
    #     self.color ="rusty"

    def __init__(self, model , color):
        self.model = model
        self.color = color

    def start(self):
        print(f"the {self.color} {self.model} car is starting")


# c1 = car()
# c1.model = "tata"
# c1.color = "black"


# c2 = car()
# c2.model ="mustang "
# c2.color ="white"

# c1.start()
# c2.start()
# c3 = car()
# c3.start()

# c4=car()
# c4.color = "violet"
# c4.start()

c5 = car("red","ferrari")
c5.start()








