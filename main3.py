N1= input("enter your n1 : ")
N2= input("enter your n2 : ")

print(int(N1)+ int(N2))


age= abs(int(input("enter your age :" )))
print(age)
weight=int(input("enter your weight in kg : "))
print(weight)

height=int(input("enter your height in cm : "))
print(height)

BMR=" 88.362 + (13.397)*weight +(4.799*height)-(5.677*age)"
bmr=eval(BMR)
print(int(bmr))