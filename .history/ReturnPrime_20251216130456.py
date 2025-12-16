# //Take a list of numbers and return a new list with only prime numbers

def ret_onlyPrime(data):
    prime= []
    
    for i in data:
        count=0
        for j in range(1,i):
            if i % j == 0:
                count= count +1
                if(count ) 

    return prime



numbers= [1,2,3,4,5,6,7,8,9]
print("The return List of only Prime", ret_onlyPrime(numbers))