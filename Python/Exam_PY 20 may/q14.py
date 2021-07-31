#1.a
import numpy as np
from scipy import linalg
A=np.array([[3,2],[1,-1]])
B = np.array([ [1, 2] ])
B=B.T
X=linalg.solve(A,B)
print("x=",int(X[0]),"and y=",int(X[1]))


#2
import numpy as np
n_array = np.array([[4, -2], [1, -3]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.inv(n_array)
print("Inverse of given 2X2 matrix:")
print(det)

#3
import numpy as np
n_array = np.array([[2, -1, 0], [0, 3, -2], [1, 0, 1]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("\nDeterminant of given 2X2 matrix:")
print(int(det))