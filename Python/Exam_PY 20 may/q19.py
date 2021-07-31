#1.a
import numpy as np
from scipy import linalg
A=np.array([[3,2],[1,-1]])
B = np.array([ [1, 2] ])
B=B.T
X=linalg.solve(A,B)
print("x=",int(X[0]),"and y=",int(X[1]))

#1.b
import numpy as np
from scipy import linalg
A=np.array([[1,3,10],[2, 12, 7],[5, 8, 3]])
B=np.array([[10, 18, 30]])
B=B.T
X=linalg.solve(A,B)
print("x = ",int(X[0]),"and y = ",int(X[1])," and z = ",int(X[2]))

#2.a
import numpy as np
n_array = np.array([[-6, -8], [4, 4]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("\nDeterminant of given 2X2 matrix:")
print(int(det))

#2.b
import numpy as np
n_array = np.array([[3, 0, 1], [4, 1, -2], [2, -2, 1]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("\nDeterminant of given 2X2 matrix:")
print(int(det))