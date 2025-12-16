def gcd(a, b):
    num1=[]
    num2=[]
    for i in range(a+1):
        if(a % i == 0):
            num1.append(i)
    for i in range(b+1):
        if(b % i == 0):
            num2.append(i)
    
    print