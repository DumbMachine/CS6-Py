def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
  
s = input("Enter the String you want to check : ")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
