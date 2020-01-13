import numpy
A=numpy.arange(1,26).reshape(5,5)
B=A.diagonal().sum()
print(B)