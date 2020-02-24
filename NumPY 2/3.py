import numpy as np
z= np.random.random((10,3))
x,y,h = z[:,0], z[:,1], z[:, 2]
r = np.sqrt(x**2+y**2+h**2)
t = np.arctan2(y,x)
print(r)
print(t)
print(h)
