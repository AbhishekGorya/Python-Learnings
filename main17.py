#numpy contails advance maths matics funcs like use of array and matrices
import numpy as NP


#creating numpy array using a list
arr = NP.array([1,2,3,4,5,6,7,8,9,0])
print(arr)
print(type(arr))


#usins atuple to create a numpy array

arr = NP.array((1,2,3,4,5,5,6))
print(arr)


#dimensions in array 1 to n
arr = NP.array(20)
print(arr) # 0 dimensional

arr = NP.array(20)
print(arr)
print(arr.ndim)



#1 d array

arr = NP.array([1,2,3,4,5,6,0,8])
print(arr)
print(arr.ndim)



#2d array
arr = NP.array([[1,2,3,4,5],[5,6,7,8,0]])
print(arr)
print(arr.ndim)


#3d
arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr)
print(arr.ndim)




arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr)
print(arr.ndim)




arr = NP.array([[[[[1,2,3,4,5]]]]])
#or arr = NP.array([1,2,3,4,5],ndimn=5)
print(arr)
print(arr.ndim)



#array indexing
arr = NP.array([1,2,3,4,5,6,0,8])
print(arr)
print(arr.ndim)

print(arr[0])


arr = NP.array([[1,2,3,4,5],[5,6,7,8,0]])
print(arr)
print(arr.ndim)

print(arr[1][2])




arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr)
print(arr.ndim)
print(arr[1][1][4]) #[z][x][y]


#addin first and last element
print(arr[0][0][0] + arr[1][1][4])




#slicing in arrays

#in 1d array

arr = NP.array([1,2,3,4,5,6,0,8])
print(arr)
print(arr.ndim)

print(arr[2:6])
print(arr[::2])



# in 2d array

arr = NP.array([[1,2,3,4,5],[5,6,7,8,0]])
print(arr)
print(arr.ndim)

print(arr[0][2:])

print(arr[0][::2])


#in 3d array
arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr)
print(arr.ndim)
print(arr[1][0][2:])  #or
print(arr[1,0,2:5])

print(arr[1,0,::2])





#data types and operations
#i int , b boolean , u unsigned int , f flot , c complex float, m timedelta
#M timeline , o object , S string , u unicode string , v fixed chunk of memory for other type (void)


# checking data type of array

arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr.dtype)

#creating array with defined data type

arr =  NP.array([1,2,3,4,5], dtype='S')
print(arr)
print(arr.dtype)

#creatin a array with data type 4 byte int
arr =  NP.array([1,2,3,4,5], dtype='i4')
print(arr)
print(arr.dtype)


#numpy array shape : the shape of an array is the  no of elements in each dimension

arr = NP.array([[3,4,5,6,4],[5,7,8,96,4]])
print(arr)
print(arr.ndim)

print("the shape of the 2d array;", arr.shape)


#for 3d array
arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr.shape)


#joining two numpy arrays
arr =  NP.array([1,2,3,4,5])
arr2 =  NP.array([6,7,8,9,0])

a = NP.concatenate((arr,arr2))
print(a)

#for 2d

arr1 = NP.array([[3,4,5,6,4],[5,7,8,96,4]])
arr2 = NP.array([[31,42,544,67,47],[56,57,48,96,34]])
a = NP.concatenate((arr1,arr2))
b = NP.concatenate((arr1,arr2),axis=1)
c = NP.concatenate((arr1,arr2),axis=0)
print(a)
print(b)
print(c)



#3d array
arr1= NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
arr2 = NP.array([[[10,20,30,40,50],[50,60,70,80,00]], [[30,40,50,60,40],[50,7,80,96,40]]])

# a = NP.concatenate((arr1,arr2))
# print(a)
a = NP.concatenate((arr1,arr2))
b = NP.concatenate((arr1,arr2),axis=1)
c = NP.concatenate((arr1,arr2),axis=0)
print(a)
print(b)
print(c)



#spiliting numopy array
#1d
arr =  NP.array([1,2,3,4,5,6])
arr2 =  NP.array_split(arr,3)
print(arr2)
#spilitting the array in 3 parts

#ravel and flatter
#convers multi dimensional array into 1d array

arr = NP.array([[[1,2,3,4,5],[5,6,7,8,0]], [[3,4,5,6,4],[5,7,8,96,4]]])
print(arr.shape)

n=arr.ravel()

print(n.shape)
print(n)


n=arr.flatten() # same as ravel


c = NP.array([[[[1,2,3,4],[23,45,6,7],[54,56,76,78]]]])
print(c)
print(c.ndim)
print(c.shape)
u = (c.ravel())
print(u)

#unique function
arr =  NP.array([1,2,3,4,5,6,7,5,3,2,1,1,1,1,2,3,43,4,1,2,3,4,5,6])
#uniques values in array
cx = NP.unique(arr)
print(cx)

cx = NP.unique(arr,return_index=True,return_counts=1 , return_inverse=1)
print(cx)




arr =  NP.array([1,2,3,4,5,6])

cx = NP.unique(arr,return_index=True,return_counts=1 , return_inverse=1)
print(cx)

#deleting a element

arr =  NP.array([1,2,3,4,5,6])
d = NP.delete(arr,[2])
print(d)

#for 2d
arr1 = NP.array([[3,4,5,6,4],[5,7,8,96,4]])
d = NP.delete(arr1 ,0,axis=0)
print(d)



