from numpy import *
import numpy as np

#array creation
# arr = array([1,2,3,4,5,6], int)  # one dimentional array
# print(arr)
#
# # linspace
# arr1 = linspace(0,15) # if we don't specify the parts it will divide into 50 times by default
# print(arr1)
#
# arr2 = linspace(0,15,20) # if we specify the total number of parts it will divide into 20
# print(arr2)
#
# arrr =np.linspace(10,100,10, endpoint=False, retstep=True) #retstep will show how much it's been divided with
# print(arrr)

# #arange
# arr3 = arange(1,15,1)
# print(arr3)
#
# #logspace
# arr4 = logspace(1,40,5)
# print(arr4)
#
# #zeros
# arr5 = zeros(5)
# print(arr5)
#
# #ones
# arr6 = ones(5, int)
# print(arr6)
#
# #copy array
# arr1 = array([1,2,3,4,5])
# arr2 = arr1.vew() # will change the address for arr2
# print(arr2)
# print(id(arr2))

#shallow copy if, we change the arr1 elements it will also change the arr2 element and this is called as shallow copy
nrr3 = array([1,2,3,4,5])
nrr4 = array([1,2,3,4,5])
nrr3[1] = 6
print(nrr4)
print(id(nrr4))

#Deep copy:-
prr3 = array([1,2,3,4,5])
prr4 = prr3.copy()

prr3[1] = 6

print(prr3)
print(prr4)


#one dimentions array:-
trr = np.array(10)
print(trr)
print(type(trr))

#two dimentional array:-
trr2 = np.array([[20,30,40], [50,60,70]])
print(trr2[1][0])

#three dimentional array
trr3 = np.array([[[20,30],[40,50]], [[60,70],[80,90]]])
print(trr3[1][0][1])

#covert the list into array with row major order
ttr = [[1,2,3,4],[5,6,7,8]]
trr4 = np.asarray(ttr, order='C') #'c' meance row major order
print(trr4)

for v in np.nditer(trr4):
    print(v)

#covert the list into array with column major order
ttr1 = [[1,2,3,4],[5,6,7,8]]
trr5 = np.asarray(ttr, order='F') #'F' meance cloumn major order
print(trr5)

for e in np.nditer(trr5):
    print(e)

#from buffer
l = b"welcome to numpy"
print(np.frombuffer(l, dtype='S1', offset=9))

#from itter
t = [10,20,30,40]
print(np.fromiter(t, dtype=float, count=2))

#reshape
s = [10,11,12,13,14,15]
z = np.asarray(s, dtype=int)
print(z)
print(z.reshape(2,3)) # reshape can be changed from single dimetional to multi-dimentional




