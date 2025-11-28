# polymorphism

#with function

class  bird:
    def fly(self):
        print("the bird is flying")

class  aeroplane:
    def fly(self):
        print("the aeroplane is flying")

    

b = bird()
a = aeroplane()

b.fly()
a.fly()




#types : compiletime(operator and function overloading) and runtime(method overriding)

#runtime 
# child class functions overrides parent class functions

class p_animal:
    def sound(self):
        print("make sound parent")


class c_animal(p_animal):
    def sound(self):
        print("make sound child")


class t_animal(p_animal):
    def sound(self):
        print("make sound t-child")


p = p_animal()
q= c_animal()
r=t_animal()

p.sound()
q.sound()
r.sound()

#same function from parent clss in overrided in child class and child class func will have precedence to be executed after ingeritance



#compile time

#run time : method overriding 
#compiule time: overloading

#not supported in python directly but  can be implemented using default argument

class calculator:
    def add(self,a,b,c=0):
        print(a+b+c)


calc = calculator()
calc.add(4,5,6)
calc.add(9,8)



#polymorphism in real world scenario


class media:
    def play(self):
        print("the media file is playing")

class audio(media):
    def play(self):
        print("the audio(media) file is playing")


class video(media):
    def play(self):
        print("the video(media) file is playing")


a = media()
b = audio()
c = video()

a.play()
b.play()
c.play()