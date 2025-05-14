import numpy as np
import statistics as stat

'''
# Create array
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
'''

'''
# Math operation
arr1 = np.array([2,4,6])
arr2 = np.array([2,4,6])
arr3 = np.array([4])

print(arr1+arr2)
print(arr1*arr2)
print(np.power(arr1,arr3))
print(np.sqrt(arr3))
'''



'''
# Slicing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,0:2])
'''

'''
# Methods
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr)) # Number of dimension 
print(arr.dtype) # Data type
'''

'''
arr = np.array([[1,2],[4,5]])
arr2 = np.array([[5,5],[6,6]])
print(np.vstack([arr,arr2])) # Vertical concatenation 
print(np.hstack([arr,arr2])) # Horizontal concatenation
'''

'''
a = np.array([[1,2],[4,5]])
print(np.append(a,[6,7])) # add in the last
print(np.insert(a,1,3)) # array,index,value
print(np.delete(a,1)) # deletation
'''

'''
ar = np.array([[2,7,1],[6,9,3]])
ar2 = np.array([10,20,30,40])
print(np.sort(ar)) # sorting
print(np.where(ar==3)) # searching

fa = ar2>20
new = ar2[fa]
print(new)
'''

'''
# Aggregating function 
ar = np.array([10,20,30,40])
print(np.sum(ar))
print(np.max(ar))
print(np.min(ar))
print(np.mean(ar))
print(np.size(ar))
'''

'''
# cumulative price 
price = np.array([100,200,300])
quantity = np.array([5,8,3])

temp = np.cumprod([price,quantity],axis=0)

print(temp)
print(temp[1].sum())
'''

'''
# statistical methods
baked_food = np.array([100,305,500,100])

print(np.mean(baked_food)) # sum of values/number of values
print(np.median(baked_food)) # center value after sorting
print(stat.mode(baked_food)) # mode only works with statistics library

price = [100,200,300]
sales = [10,20,8]

print(np.corrcoef([price,sales])) # corelation , coeffitient
'''


