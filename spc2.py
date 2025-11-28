# def num(n):
#     count = 0
#     for i in n:
#         if i in range(90, 101):
#             print(f"the grade of student{count+1} is A")
#             count+=1
#         elif i in range(80, 90):
#             print(f"the grade of student{count+1} is B") 
#             count+=1
#         elif i in range(70, 80):
#             print(f"the grade of student{count+1} is C")
#             count+=1 
#         elif i in range(60, 70):
#             print(f"the grade of student{count+1} is D")
#             count+=1
#         elif i in range(0,60):
#             print(f"the student{count+1} is failed ")
#             count+=1 
#         else:
#             print("the students score entered is invalid")
#             count+=1
            

# list = [90,98,44,33,4,44,22,22,55,42,902]
# num(list)
        
# import random





# def chk_function():
#     secretnum = random.randint(0,100)
    
#     print("welcome to the number guessing game")
#     print("i have choosen the number between 1 to 100 , Can you guess it ")

#     attempts = 0
#     guess = None

#     while guess != secretnum:
#         guess= int(input("enter your guess"))
#         attempts+=1
#         if guess < secretnum:
#             print("too low , try again")
#         elif guess> secretnum:
#             print("too high , try again")
#         else:
#             print("you have guessed the correct number ")
#             print("the no of attemps to find out the number is ",attempts)
#             chk_function()
    
# chk_function()



num = abs(int(input("Enter n numbers to calculate the sum of ")))

def func_for_squares(n):
    sum=0
    for i in range(num):
        sum = sum + ((i+1)*(i+1))

    print(f"the sum of square of n numbers is {sum}")


func_for_squares(num)