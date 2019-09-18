import numpy as np


a = np.array([1, 3, 5, 7, 9])
b = np.array([2, 4, 6, 8, 10])
c = a+b
print(c)                                # [ 3  7 11 15 19]
c = a-b
print(c)                                # [-1 -1 -1 -1 -1]
c = a*b
print(c)                                # [ 2 12 30 56 90]
c = a/b
print(c)                                # [0.5        0.75       0.83333333 0.875      0.9       ]
c = a+10
print(c)                                # [11 13 15 17 19]
c = a*10
print(c)                                # [10 30 50 70 90]
c = a @ b                               # dot product of two matrix
print(c)                                # 190
c = np.dot(a, b)
print(c)                                # 190
print(a.size)                           # 5
print(a.ndim)                           # 1
print(a.shape)                          # (5,1)
print(type(b))                          # <class 'numpy.ndarray'>
slice_array = a[1:4]
print(slice_array)                            # [3,5,7]
slice_array = a[1:-1]
print(slice_array)                            # [3,5,7]
slice_array = a[1:4:2]
print(slice_array)                            # [3,7]
