# inheritance
#single 

class parent:
    def show(self):
        print("this is parent clase")

class child(parent):
    def display(self):
        print("this is child clase")

a = child()
a.show()
a.display()


#multiple
class parent1:
    def show1(self):
        print("this is parent1 clase")

class parent2:
    def show2(self):
        print("this is parent2 clase")

class child(parent1,parent2):
    def display(self):
        print("this is child clase")
    
a = child()
a.show1()
a.show2()
a.display()



#multilevel

class G_parent:
    def G_show(self):
        print("this is G_parent clase")

class parent(G_parent):
    def show(self):
        print("this is parent clase")

class child(parent):
    def display(self):
        print("this is child clase")

a = child()
a.G_show()
a.show()
a.display()



#hieracrchical

class parent(G_parent):
    def show(self):
        print("this is parent clase")

class child1(parent):
    def display1(self):
        print("this is child1 clase")

class child2(parent):
    def display2(self):
        print("this is child2 clase")


a = child1()
b= child2()

a.display1()
a.show()

b.display2()
b.show()



#Hybrid multilevel + multiple

class G_parent:
    def G_show(self):
        print("this is G_parent clase")

class parent1(G_parent):
    def show1(self):
        print("this is parent1 clase")
class parent2:
    def show2(self):
        print("this is parent2 clase")


class child(parent1,parent2):
    def display(self):
        print("this is child clase")

a = child()
a.display()
a.show1()
a.show2()
a.G_show()


