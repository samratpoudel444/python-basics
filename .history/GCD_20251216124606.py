def gcd(a, b):
    num1=[]
    num2=[]

    if(a ==0 or b== 0):
        print("the Gcd is 0")

    else:
        for i in range(1,a+1):
            if(a % i == 0):
                num1.append(i)
        for i in range(1, b+1):
            if(b % i == 0):
                num2.append(i)
    
    for i in range(num1):
        for j in range(num2)

gcd(12,8)