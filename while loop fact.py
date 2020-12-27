print("Factorial Calculater")
while(True):	
    number = int(input("Please enter a number: "))
#Ali Bahadır Şensöz   
    fact = 1
    i = 1
     
    while i <= number:
            fact = fact * i
            i = i + 1
     
    print("The factorial of ", number, " is ", fact)
