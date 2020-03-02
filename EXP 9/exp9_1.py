string = "Test String"

upper , lower = 0, 0

for c in string:
    if c.isupper():
        upper += 1 
    elif c.islower():
        lower += 1 
        
print("Upper:", upper, "Lower:", lower)
