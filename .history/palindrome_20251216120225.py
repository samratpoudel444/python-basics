number= 1001

data= number
revNumber=0

do data != 0:
    remainder= data % 10
    data= data // 10
    revNumber= revNumber*10 + remainder

print(revNumber) 