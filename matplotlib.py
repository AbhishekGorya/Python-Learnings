#2d graphs 
#complete visualization



import matplotlib.pyplot as M

#linear chart
#scatter plo
#stem plot
#step plot
#hist /bar plot
#box ploat
#area plot
#sub plot : combination of two or more line




import pandas as D






#linear graph

x = [1,2,3,4,5,6,7]
y = [8,9,10,11,12,13,14]

M.plot(x,y)
#plot linear graphs
M.show()
#graph without descriptive line


#changing color of linear graph

color = 'r' #red
M.plot(x,y,color)
M.show()


#changing values
x = [5,4,7,7,4,2,2,2]
y = [6,8,9,6.3,5,3,2]

M.plot(x,y)


#with dots and markers
M.plot(x,y,marker='.')
#marker highlights coordinate points

M.show()




#x diierent line and y point as markers
M.plot(x,y,marker='.') # both x and y coordinates are plotted accordingly
M.plot(y, maker = '>')# only y chart with line and a markers
M.plot(x, maker = 'x')# only x chart with line and a markers
M.show()




#bar graph


x = [1,2,3,4,5,6,7]
y = [8,9,10,11,12,13,14]

M.plot(x,y)
M.show()


color = ['r', 'g' , 'y' , 'p']
M.bar(x,y , color)#coloring bars differently


#bar graph horizontly
#using array D

x = D.array(['a', 'b','c','d','e'])
y = D.array(['f', 'g','h','i','j'])

M.bar(x,y , color='')  #you can also input color codes
#veritical
M.barh(x,y , color='red')
#horizontal
M.show()




#width of bars
M.barh(x,y , color='red' , width=3)

M.show()



#height of bars

M.barh(x,y , color='red' , height = 0.1)
#for horizontal bars
M.show()






#scatter plot

x = [1,2,3,4,5,6,7]
y = [8,9,10,11,12,13,14]



#title for the graph

M.title("Scatte")
M.scatter(x,y, color = 'r')
#or 
c = ['red','blue','green','violet','yellow','black']
M.scatter(x,y,c)
M.show()




#labels for axises
M.xlabel("lulu")
M.ylabel("bulu")



##size of scatter plot
M.scatter(x,y,c,s= 130)
#changes the size of bubbles



#woring with images 
#part t20 matplotlib


#chaning color of a image  using matplotlib

import matplotlib.pyplot as M
import numpy as N
from PIL import Image


fname = r'lullu.jpg'
#opeing image using PIl
image = Image.open(fname).convert('L')#l (covert to differnrt forms or rgb(exact image)

#mapping image to gray scale
M.imshow(image , cmap = 'grey')


# same for png file
M.imshow(image , cmap = 'coolwarm')
#or there are multilple colors themes

#images as a graph 


#to save image savefig() is used



M.savefig(image)
M.title('salman khan ')
#for plots name
M.show()



M.xlabel('lulu')
M.ylabel('Bulu')


#to create grid()
M.grid()
M.show()




#pie chart


x =  ['a','b','c','d','e','f']
y = [10,20,30,40,59,99]
M.pie(y , labels=x)
M.show()

c = []#colors]
M.pie(y , labels=x , colors= c)
M.legend() # gives labels with respective colors



#changing color of labels or fonts


































