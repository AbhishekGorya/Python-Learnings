a=34
b=98
c=216



#soln1
exp = input("enter the expression you wnat to evaluate: ")
result = eval(exp)
print("your final output for the expression is ", int(result))

#soln2
u1 = float(input("enter house size H1"))
u1r = int(input("enter room in H1"))
price1=float(input("enter the budget for H1"))

u2 = float(input("enter house size H2"))
u2r = int(input("enter room in H2"))
price2=float(input("enter the budget for H2"))

H1price= u1*5000
print("the price for H1 is ", H1price)
H2price= u2*5000
print("the price for H2 is ", H2price)

th=7500000


u1_th=H1price>=th
u2_th=H2price>=th
print(f"u1 is paying above threshols ",{u1_th})
print(f"u2 is paying above threshols ",{u2_th})





#soln2
u1 = float(input("enter house size H1"))
u1r = int(input("enter room in H1"))
price1=float(input("enter the budget for H1"))

u2 = float(input("enter house size H2"))
u2r = int(input("enter room in H2"))
price2=float(input("enter the budget for H2"))

H1price= u1*5000
print("the price for H1 is ", H1price)
H2price= u2*5000
print("the price for H2 is ", H2price)

th=7500000


u1_th=H1price>=th
u2_th=H2price>=th
print(f"u1 is paying above threshols ",{u1_th})
print(f"u2 is paying above threshols ",{u2_th})









stsym = input("enter stock symbol ")
cprice = float(input("enter current price of symbol "))
pchange= float(input("enter percentage change "))
fprice= cprice+pchange*cprice

print("aftre change the price bcomes to be ",fprice)

budget = float(input("enter the budget "))

comparison = fprice<= budget

print(f"the price of stock is lesser than budget ",{comparison })








ctemp=int(input("enter the current tempreture "))
mintemp = 25
maxtemp = 50

rangechk = mintemp < ctemp < maxtemp

print(f"the current tempreture is within the range ",{rangechk})
