d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n = int(input("Enter the key value to be found\n"))
if n in d:
    print("Key is present in dict")
else:  
    print("Key is not present in dict")
