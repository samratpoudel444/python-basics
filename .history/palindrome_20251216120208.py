number= 1001

data= number
revNumber=0

if data != 0:
    remainder= data % 10
    print(remainder)
    data= data // 10
    print(data)

print(revNumber) 