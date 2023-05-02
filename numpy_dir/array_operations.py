import numpy as np

#sort operation (column)
a = np.array([[20,50,70],[50,30,40]])
z = np.sort(a, axis=0) #axis  = 0 indicates column wise sorting
print(z)

#sort operation (row)
b = np.array([[20,50,70],[50,30,40]])
y = np.sort(a, axis=1) #axis  = 1 indicates row wise sorting
print(y)

#sort different data types
arr = np.dtype([('name','S1'),('percent',float)])
arr1 = np.array([('ramu', 95.0),('any', 93.0),('raju', 97.5)],dtype=arr)
print(np.sort(arr1,order='percent'))

#append of array
att = np.array([1,2,3,4])
att1 = np.array([5,6,7,8])
e = np.append(att,att1)
print(e)

