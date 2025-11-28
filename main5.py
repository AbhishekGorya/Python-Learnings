#conditional statements
# i=20;
# if i>10:
#     print("20is greater than 10")
# print("conditioan is false")

import math

# tempreture=float(input("enter the tempreture "))
# if tempreture<15:
#     print("tempreture is nor good enough")
# if 20<tempreture<28:
#     print("tempreture is optimal")



# age=int(input("enter your age"))
# if age>=18:
#     print("you are elligible to vote")
# else:
#     print("paida hi huye ho abhi")


# b_sal=int(input("enter your bare salary"))
# b_dura=int(input("enter no of years you have been working here"))

# if b_dura>5:
#     int_sal= b_sal+0.08 * b_sal
#     new_sal = int_sal - 0.12 *int_sal
#     print("your final saloary after texes and binus is ",new_sal)
# else:
#     print("your are not eligible for any  bonus and salary will be ", b_sal-b_sal*0.12)


# city=input("enter a city name and according to the name of city its codename will be printed : ")

# if city=="mumbai":
#     print("the city code is C1")
# elif city=="kolkata":
#     print('the city code is C2')
# elif city=="chennai":
#     print('the city code is C3')
# elif city=="banglore":
#     print('the city code is C4')
# elif city=="pune":
#     print('the city code is C5')
# else:
#     print("Unknown city")



#while loop

# count = 1;
# while count <= 50 :
#     if count%2==0:
#         print(count)
#     count+=1

# email = input("enter your email id ")

# valid_mail=False;
# while not valid_mail:
#     if "@" in email and "." in email:
#         print("valid email")
#         valid_mail= True
#     else:
#         print("try again")
#         email=input("enter your email id")



# em = input("enter a valid amin address")

# valid = False

# while not valid:
#     if "@" in email and "." in email:
#         print("valid email")
#         valid= True
#     else:
#         print("invalid email address")
#         em = input("tray again and input valid email address")



#for loop
# number = [1,2,3,4,5,6]
# for i in number:
#     print(i)

# str = "lullubyyyyyyyy"
# for i in str:
#     print(i)

# for i  in range(11):# digit + 1
#     print(i)

# for i in range(5,26):
#     print(i)


# for i in range(5,91):
#     if i%5==0:
#         print(i)
#     else:
#         print("XXXXX")



# i = int(input("give a number to output its table"))
# for x in range(1,11):
#     print(f"{i} X {x} = {i*x} ")




# num= int(input("enter no. of items you want to buy now"))

# total_price= 0
# for i in range(num):
#     price = float(input(f"enter the price of item {i+1}"))
#     total_price+=price

# if total_price>=100:
#     discount = 0.1 * total_price
# elif 50<=total_price<100:
#     discount =0.5*total_price
# else:
#     discount = 0

# total_bill= total_price - discount


# print("total bill for the purchase is ",total_bill)


# for i in range(1,11):
#     if i==7:
#         break
#     print(i)


# for i in range(1,11):
#     if i==7:
#         continue
#     print(i)


def func():
    print("hello im abhissheh")

func()





# def bill_pay():
#     print("the last day for the bill payment is next week sunday ")
#     print("after deadline , youll not be able to use lights")
#     print("pay your bill soon")

# for i in range (3):
#     a = input("enter your name ")
#     b= int(input("enter units comsumed by user 1"))
#     bill = b * 10
#     print(f"the total bill for the user{i+1} is {bill}")
#     bill_pay()









# def chk(num1):
    
#     if num1%2==0 :
#         print("the entered number is evn")
#     else:
#         print("odd")

# num1 = int(input("enter a number to check if the number is evn or odd"))

# chk(num1)


# def myname(fname , lname):
#     print(fname +" "+lname)

# a= "rahuklkllll ki"
# b="maa ki ch******"

# myname(a,b)

exam_score=[78,31,98,90,99,23,34,75,99,87]

def score_card(lists):
    nums = len(lists)
    print(f"the average score of the students is {sum(exam_score)/nums}")
    print(f"the maximum score from the students is {max(lists)}")
    print(f"the minimum score from the students is {min(lists)}")
    
    students_passed=0
    students_failed=0
    for i in lists:
        if i>=80:
            students_passed+=1

        else:
            students_failed+=1
    print("total students passed are ",students_passed)
    print("total students failed are ",students_failed)   
score_card(exam_score)  
