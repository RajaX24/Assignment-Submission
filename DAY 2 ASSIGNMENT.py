"""#DAY 2 ASSIGNMENT

###Write a program to find the prime number
"""

a=[1,2,3,4,5,6,7,8,9,10,11,25,54,78,741]
for i in range(0,15):
    if (a[i] %2) == 0:
            print(a[i], "is not a prime number")
    else:
            print(a[i], "is a prime number")

"""###Enter a number to program and get the output "Prime" or "Not Prime"""""

def primenumber(a):  
  
    if a > 1:  
       
        for i in range(2, int(a/2) + 1):  
            
            if (a % i) == 0:  
                print(a, "is not a prime number")  
                break  
      
        else:  
            print(a, "is a prime number")  
   
    else:  
        print(a, "is not a prime number")  

a = int(input("Enter an input number:"))  
 
primenumber(a)
