import numpy as np
a1=np.array([1,2,3,4,5])
print(a1)
# print(type(a1))
a1=np.array((1,2,3,4,5))
print(a1)
print(type(a1))



a2=np.array([[2,3],[4,5],[5,3]])
print(a2)

a3=np.array([[2,3],[4.5,5],["5",3]])
print(a3)

a4=np.array( [ [ [2,3],[4,5],[5,3] ], [ [2,3],[4,5],[5,3] ] ] )
print(a4)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
print(a4.dtype)

a5=np.array([1,2,3],dtype="f")
print(a5)
print(a5.dtype)

a6=np.array([1,2,3,4.5,"o"],dtype="S")
print(a6)
print(a6.dtype)

a7=np.array([1,2,3,4.5,"o"])
print(a7.dtype)
