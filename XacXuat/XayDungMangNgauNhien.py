import numpy as np

#numpy.random.rand
a = np.random.rand()
b = np.random.rand(4)  # Mảng có 1x8 phần tử
c = np.random.rand(2, 3)  # Mảng có 2x3 phần tử

print("a = ", a)
print("b = ", b)
print("c = ", c)

#numpy.random.seed

e = np.random
e.seed(10)

print("e rand: ", e.rand())

#numpy.random.normal

m, sigma = 0, 0.1 # mean và standard deviation
s = np.random.normal(m, sigma, size=15)
print("s = ", s)

#numpy.random.randn

t = np.random.randn(3, 3)
print("t = ", t)

#numpy.random.uniform

u = np.random.uniform(size=4)
print("u = ",u)

#numpy.random.permutation
w = np.random.permutation(10)
print("w = ", w)