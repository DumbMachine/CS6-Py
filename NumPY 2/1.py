import numpy as np
x = np.arange(10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = eval(input("Enter the value of n:"))
print (x[np.argsort(x)[-n:]])
