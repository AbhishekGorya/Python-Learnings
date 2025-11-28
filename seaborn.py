#for statistical graphs 
# like mean mode median


#built on matplotlib and pandas




import seaborn as S


#relational (x and y) , categoraial (multiple elements of different categories) , distribution plots

#also regression and matrix and multi-plot graphs




import seaborn as s
import matplotlib.pyplot as m


v1 = [1,2,3,4,5,6]
v2 = [7,8,9,10,11,12]

#graph same with matplotlib and also with seaborn


#with matplotlib
m.plot(v1,v2)
m.show()


#with seaborn
s.lineplot(x=v1,y=v2)
m.show()


#for datasets always use pandas
import pandas as p 


#datframe

df = p.dataframe({"keys":v1 , "values":v2})

df



# plotting line graph from data frame to line graph using seaborn
s.lineplot(x=v1, y=v2 , data=df)
#advance graph with alos labels on graph as it was not in matplotlib

#means seaborn library has additional details for the matplotlib graphs




#now learning with anothe datasets penguin.csv from iscale github
#using seabron
df1 = s.load_dataset('penguin')

df1



#making line plot using data set cols
s.lineplot(x="bill_length_mm" , y="flipper_length_mm" , data = df1)
m.show()

#withs labels by default


#now dividing bill and flipper length based on penguins gender
#upper graph divided based on gender
#categorial

s.lineplot(x="bill_length_mm" , y="flipper_length_mm" , data = df1 , hue ='sex') #hue is ctegorial
m.show()




#more parametrs to be passed

#colors to the lines in line plot according to the user
s.lineplot(x="bill_length_mm" , y="flipper_length_mm" , data = df1 , hue ='sex' , palette = 'rocket_r') #palette for changing colors


#adding coordinates to the line # with using markets parameter

s.lineplot(x="bill_length_mm" , y="flipper_length_mm" , data = df1 , hue ='sex' , style = 'sex', markers=['@','&'])
 #style for applying markers
 
 
#trimming data from datasets
df1 = s.load_dataset('penguin').head(20)
#only 20 rows from data set will be displayed now




#grids

s.lineplot(x="bill_length_mm" , y="flipper_length_mm" , data = df1 , hue ='sex' , style = 'sex', markers=['@','&'] , grid = True)
#or 
m.show()



#adding title to the graph
m.title("This is a line graph for penguins datasets ")

m.show()









#############part 2#####################


#bar bgraph using seaborn

import seaborn as s

import matplotlib.pyplot as m
import pandas as p
#importing matplotlib and pandas as seaborn is made on it

#and pandas coz we'll working on data sets


# search "seaborn dataset github"  and choose any 
# we'll be using penguins
# 
# 
# 
# 




df = s.load_dataset("penguins")

df



#bar graph

df1['islands']   #colmn for bar representation
#for x axis


#bill length for y axis
s.barplot(x = df.island , y= df.bill_length_mm)
m.show()


#another method for same plot
s.barplot(x='island' , y='bill_length_mm' , data = df)


m.show()





#getting gender division for above senerio #categorial division
#for that hue parameter is used
s.barplot(x='island' , y='bill_length_mm' , data = df , hue='sex') #sex is another col using for categorial division




m.show()




#ordering bars in the chart plot


order1 = ['dream','torgersen','biscoe island']     #ordering x axis data


s.barplot(x='island' , y='bill_length_mm' , data = df , order=order1)


m.show()





#by default the x axis has m-f  order now we have to do it f-m
#use hue_order

s.barplot(x='island' , y='bill_length_mm' , data = df , hue='sex' , order = order1 , hue_order = ['Female','Male'])


m.show()











#changing the color of the masle and female bars on the x-axis


s.barplot(x='island' , y='bill_length_mm' , data = df , hue='sex' , order = order1 , hue_order = ['Female','Male'] , palette = 'accent' )
#for two values use two colors but you can also use multiple colors in form of list
#palette papameter is used to color bars or graphs in seaborn
m.show()







#saturation parameter in seaborn
s.barplot(x='island' , y='bill_length_mm' , data = df , hue='sex' , order = order1 , hue_order = ['Female','Male'] , palette = 'accent' , saturation = 0.7 )
#used to adjust saturation of the bars
#value from 0 to 1
m.show()





#histogram in seaborn library
#there is no gap btw bars as it is in bar chart


#problem you want flipper_length_mm on the x axis and its count on the y axis

#in matplot lib ist_plot() but distplot() in seaborn
s.displot(df["Flipper_length_mm"])
m.show()


#count is display on its own

#problem is that not all the bar x axis lables are alligned correctly for solving this
#proper intervelling

#for this use bins parametre


s.displot(df["Flipper_length_mm"], bins=[170,180,190,200,210,220,230])
#labels interval accordin to the user
m.show()



#changing colors of the list using color papameter

s.displot(df["Flipper_length_mm"] , color = 'red')
m.show()




#kernel density (kde) parameter : which is used used to show how much hike have gone and how much lower from one point to another


s.displot(df["Flipper_length_mm"], bins=[170,180,190,200,210,220,230] , color='green' , kde = True)

