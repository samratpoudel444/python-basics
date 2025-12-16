number= 1001

data= number
revNumber=0

ifdata != 0):
    remainder= data % 10
    print(remainder)
    data= data // 10
    print(data)
    revNumber= revNumber*10 + remainder

print(revNumber) 