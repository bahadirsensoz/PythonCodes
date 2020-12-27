print("PRIME NUMBER INDICATER") 
while(True):
    a=int(input("Please enter a number:"))
    b = a-1
    isPrime = 1
#Ali Bahadır Şensöz
    while b!=1:
        if a%b == 0:
            isPrime = 0
            print(a, " is not a prime number.")
            print(b, " times", a//b, "is", str(a) + ".")
            break
        b = b-1
    if isPrime == 1:
        print(a, " is a prime number.")


