import numpy
A=numpy.arange(1,26).reshape(5,5)
B=[row[0] for row in A]
print(B)