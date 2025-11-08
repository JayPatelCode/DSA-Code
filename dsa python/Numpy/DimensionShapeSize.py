import numpy as np
a1=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a1)
print(a1.dtype)
print(type(a1))
print(a1.size)
print(a1.ndim)

a2=np.array([ [[], [], []], [[], [], []] ])
print(a2)
print(a2.dtype)
print(type(a2))
print(a2.size)
print(a2.ndim)

a3=np.array(32)
print(a3.size)
print(a3.ndim)



a4=np.array([1,2,3], ndmin=0)
print(a4.ndim)


a5=np.array([1,2,3], ndmin=1)
print(a5.ndim)

a6=np.array([1,2,3], ndmin=2)
print(a6.ndim)
print(a6.shape)

a7=np.array([[1,2,4,5,2,4],[1,2,4,5,2,4]])
print(a7.shape)
print(a7.ndim)

a8=np.array([1,2,4,5,2,4])
print(a8.shape)
print(a8.ndim)

a8=np.array([[[1,2,4,5,2,4], [1,2,4,5,2,4]], [[1,2,4,5,2,4], [1,2,4,5,2,4]]])
print(a8.shape)
print(a8.ndim)

# print(a1)
# print(a1.shape)

a9=np.zeros((3,2))
print(a9)

a9=np.zeros((3,1), dtype="i4")
print(a9)

a9=np.full((3,2), 3, dtype="i4")
print(a9)

a10= np.arange(5)
print(a10)