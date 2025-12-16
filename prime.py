num= int(input("Enter the number"))

sum=0
for i in range(2,num):
    if(num % i == 0):
        sum= sum+1

if sum== 0:
    print("prime")
else:
    print("composite")
