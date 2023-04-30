import numpy as np

#a)
m1 = np.array(([2, 12, 24, 100, 250],
               [1, 24, 48, 125, 400],
               [6, 36, 72, 150, 550],
               [4, 48, 96, 175, 700]))
print(m1.shape)
print(m1)

#b)
m2 = m1[[0,1,2,3],::-1]
print(m2)

#c)
m3 = m1[::-1]
print(m3)

#d)
print(m1[1:3,1:4])
