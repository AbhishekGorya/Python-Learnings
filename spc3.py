# #que n1
# d_points = [10,20,30,40,50,60,70,80,90,90000]

# d_points.append(600)
# d_points.insert(0,500)
# d_points.remove(30)
# print(d_points)



# #que n2
# # number_of_students = int(input("enter total no. of students enrolled for the course: "))

# # students_credits=[]
# # for i in range(number_of_students):
# #     credit = int(input(f"enetr the credit score for the student {i+1} : "))
# #     students_credits.append(credit)

# # print(students_credits)

# # count= 0 

# # # for i in students_credits:
# # #     if i > 12:
# # #         print(f"the student with id {count+1 } is a full time ")
        
# # #     else:
# # #         print(f"the student with id {count+1 } is a half time ")

# # #     count+=1

# # credits_status =[]
# # for i in students_credits:
# #     if i > 12:
# #         credits_status.append('fulltimer')
        
# #     else:
# #         credits_status.append('halftimer')

# # print(credits_status)
# # for i in range(number_of_students):
#     # print(f"student {i+1} : enrollment status: {credits_status[i]}")












# #que n3

# number_of_people = int(input("enter total no. of people to be grouped by their ages: "))

# peoples_ages=[]
# for i in range(number_of_people):
#     age = int(input(f"enetr age of the person with indexed {i+1}st : "))
#     peoples_ages.append(age)

# print(peoples_ages)

# child=[]
# adult=[]
# senior=[]

# for i in peoples_ages:
#     if i <18 :
#         child.append(i)
#     elif 18<= i <65:
#         adult.append(i)
#     else:
#         senior.append(i)
    
# print(child , adult , senior)

# print(f"the no of person in child grouyp from the given records: {len(child)}")

# print(f"the no of person in adult grouyp from the given records: {len(adult)}")

# print(f"the no of person in senior-citizon grouyp from the given records: {len(senior)}")




str= "hello i am abhishek and i hate coding"

STR = str.upper()

print(str)

print(STR)

words_list=STR.split()
print(words_list)

joined_list=[]
for i in words_list:
    var = i + " "
    joined_list.append(var)

print(joined_list)


modstr=''.join(joined_list)
print(modstr)





list_ages =[20,43,52,68,75,52,18,33,35,34,24,21]

asc = sorted(list_ages)
desc = sorted(list_ages,reverse=True)

print(asc)
print(desc)