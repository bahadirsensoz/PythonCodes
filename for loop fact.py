print("Factorial Calculater")
while(True):

    number = int(input("Please enter a number: "))
#Ali Bahadır Şensöz    
    fact = 1
     
    for i in range(1, number + 1):
        fact = fact * i
     
    print("Factorial of ", number, " is ", fact)
