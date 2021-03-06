# -*- coding: utf-8 -*-
"""Highradius_numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10qFdgPGZCkivOp8fAZdvPo6Y3UyLZ5OD

# Numpy
"""

import numpy as np

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
res=np.array(arr)

res

import numpy as rp
arr=rp.array([[1,2,3],[4,5,6]])
res=rp.array(arr)
res

import numpy as rp
arr=rp.array([[1,2,3],[4,5,6]])
arr

import numpy as rp
arr=rp.array([[1,2,3],[4,5,6]])
res=rp.ndim(arr)
res

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
res=np.shape(arr)

res

arr=np.array([[1,2,3],
              [4,5,6]])
res=np.size(arr)
res

arr=np.array([[1,2,3],
             [4,5,6]])
res=arr.dtype
res

arr=np.array([[0.1,0.2,0.3],
             [4,5,6]])
res=arr.dtype
res

arr=np.array([[0.1,0.2,0.3],
             [4,5,6]])
res=arr.itemsize
res

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

import numpy as np
print(np.__version__)

import numpy as np

arr = np.array({1, 2, 3, 4, 5})

print(arr)

import numpy as np
arr= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
res=arr.ndim
res

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
res=arr.dtype
res

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, :4])

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

import numpy as np

arr = np.array(['apple'])

print(arr.dtype)

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(4, 2)

print(newarr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)