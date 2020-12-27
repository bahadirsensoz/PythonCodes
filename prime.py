print("PRIME NUMBER INDICATER") 
while(True):
    a = int(input("Please enter a number: "))
    
#Ali Bahadır Şensöz   
    if a > 1:
       for b in range(2,a):
           if (a % b) == 0:
               print(a,"is not a prime number.")
               print(b,"times",a//b,"is",str(a)+ ".")
               break
       else:
           print(a,"is a prime number.")
           
    else:
       print(a,"is not a prime number.")
