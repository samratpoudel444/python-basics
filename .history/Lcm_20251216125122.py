import math

def Lcm(a,b):
    return (a*b) // math.gcd(a,b)

print("The lcm is: ",Lcm(2,3))