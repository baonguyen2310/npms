import numpy as np
print(np.__version__)

scalar = np.array(42)
print(scalar, type(scalar), scalar.ndim, scalar.dtype)
print(scalar-4, type(scalar-4), scalar.ndim, scalar.dtype)

print(np.arange(1, 10))

arr = np.array([[1.1,2,3],[0,4,5]])
print(arr, type(arr), arr.ndim, arr.dtype, arr.shape)
print(arr[0:2,0])

newarr = arr.astype("i")
print(newarr, newarr.dtype)
newarr = arr.astype(bool)
print(newarr, newarr.dtype)

copyarr = arr.copy()
viewarr = arr.view()
arr[0,0] = 1.2
arr = arr.reshape(6,-1)
vector = arr.reshape(-1)
print(arr, "\n", vector, "\n", copyarr,"\n", viewarr)

arr = np.concatenate((copyarr, viewarr), axis=1)
print(arr)

searchIndexes = np.where(arr == 4)
print(searchIndexes)
arr = np.sort(arr)
print(arr)
searchIndexes = np.searchsorted(arr[1], 4)
print(searchIndexes)

arr1 = [5, 6, 3, -8]
arr2 = [1, 2, 3, 4]
print(arr1 + arr2)
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.dot(arr1, arr2))
print(np.outer(arr1, arr2))
print(np.divide(arr1, arr2).astype(int))
print(np.remainder(arr1, arr2))
print(np.power(arr1, arr2))
print(np.absolute(arr1))

print(np.sum([arr1, arr2], axis = 1))
print(np.cumsum(arr1))
print(np.prod([arr1, arr2], axis = 1))
print(np.cumprod(arr1))

print(np.around([3.6666, -3.1666], 2))
print(np.floor([3.6666, -3.1666]))
print(np.ceil([3.6666, -3.1666]))

print(np.sin([np.pi/2, np.pi]))
print(np.deg2rad([90, 180]))

print(np.unique([1,1,1,2,2]))
print(np.union1d(arr1, arr2))
print(np.intersect1d(arr1, arr2))
