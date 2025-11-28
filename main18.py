#pandas :  panel data and python data analytics
#working with data sets
#for cleaning data
#analyse , clean , explore and manipulate data


#pandas library
import pandas as PD


#opeing a csv file to work with
a =PD.read_csv('Titanic_dataset.csv')

#to view n no od rows only
a.head()
#top 5

#bottom 5
a.tail()


a #prints data set

#printing what type of data a column comtaing
a.dtypes

#NaN : not a number or missing values


#mean max and min from a coloumn
#ang also std. deviation

a.describe()
#ONE FOR ALl
#string coloums are ignored in describe() , works for only numeric data cols


a
#prints complete table


#creating table with selective coloums 
a[['Name' , 'Sex', 'Ticket', 'Cabin' , 'Embarked']]
#no numeric int coloumn

a.dtypes ==object
#gives false if data col type is other than string



a.dtypes == 'float64'
#true for float type cols

a[a.dtypes[a.dtypes=='float64'].index]# gives cols that are containing float values

a[a.dtypes[a.dtypes=='int64'].index]# gives cols that are containing int values




#starting n cols
a.head(10)
a.tail(90)



a.columns #prints all cols

#data only from one particular col
a[['Ticket']]
#by default all rows are printed with indexing




#data only from one particular col and nor of row entreis
a[['Ticket']][4:16]
#ticket col entry from 4th to 15th
a[['Ticket']][4:16:2]
#with jumps



#for two cols
a[['Ticket','Cabin']]
a[['Ticket','Cabin']][4:16:2]



a


#creating new col with all initialised valves with 0
a[['New_col']]=0 #any value

a


#new coloum always added to the last bydefault but you can position the new coloumn

a.insert(loc = 9 , column = 'New_col2' , value = 99)

a.insert(loc = 10 , row = 'New_col3' , value = 'created')









#part2



x =a['Name'][0:10]
#name from index 1 to 10


type(x)


#indexing from user perspective according to you
i =['1','2','3','4','5','6','7','8','9'] #indexes
PD.Series(x , index = i) #inedexed for nothing


PD.Series(list(x) , index = i)





m1 = PD.Series([100,200,300,400,500], index= [1,2,3,4,5])

m1

m2 = PD.Series([600,700,800,900,1000], index= [1,2,3,4,5])

m2



#combining two indexed lists


m3 = PD.concat([m1,m2])


m3[1] #accessing element using indexing
#  100 & 600

m1*m2 #elements of particular inex are multiplied



#adding two inedexed rows
m1+m2 #same inedexelements are added






a.head()


#deleting a coloumn
a.drop("paseeengerid", axis=1)
#axis 1 for cols and 0 for rows
#tempotary delete 


#permanent delete
a.drop("paseeengerid", axis=1 , inplace=True)


#deleting a row
a.drop(3 , axis=0 , inplace=True) # 3 is default inedx


#making a coulm  a index

a.set_index("Name" , inplace=True)

   #'Name cols as a index





#resetting a index 
a.reset_index()




#dictionary to a dataframe

d = { 1:[1,2,3,4,5], 2:[2,4,5,6,7],3:[0,9,8,7,6],4:[9,6,5,4,]}

PD.DataFrame(d)  #keys will be cols 

df1 = PD.read_csv("taxonomy.csv")

df1

#NaN
#deleting a rows that have NaN entries

df1.dropna(inplace=True)
#for row axis = 0 or default

#imporant functions should be revised ones atleast

# inscale should be usd everywhere to make changes permanent


#removing cols with NaN entries
df1.dropna(axis=1 , inplace=True)






#inserting any values in place of NaN according to the user
df3 = PD.read_csv("taxonomy.csv")
df3.fillna("Noneeeeeee" , inplace = True)




