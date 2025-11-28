str = 'lubulubulubulubulubulubulubuliu'
print(type(str))
print(str)



str2 ='''i am abhishek gorya
    lubulluubb\n
    hffhrfhfbfvnfnfrfhf'''
print(str2)


str3 ='''\n\n\n\n\n\n\n\n\n\n\n\n'''
print(str3)


#indexing of strings

s= "hello dear learnerss"
print(s[5:10])
print(s[5])

print(s[-6:-1])


print(s[0],s[1],s[3],s[4],s[5])



a = "i am learning data science"
print(a[0:4])
print(a[:])
print(a[0::2]) #jump+1

#negative slicing

print(a[-6:-1])
print(a[-6:: 2])



# def extractdate(date):
#     year = int(date[0,4])
#     month = int(date[5:7])
#     days =int(date[8:])

#     return (year , month , days)

    

# extractdate("2034-67-90")



st = "honesty is the best policy"
print(st[::-1])




def func(str):
    sub_str = str[3:9]
    print(sub_str)

stt = "dataassjfjfhfjgjgj"

func(stt)