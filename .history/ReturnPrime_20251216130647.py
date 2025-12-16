def ret_onlyPrime(data):
    prime = []
    
    for i in data:
        if i > 1:  
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
            if count == 2:
                prime.append(i)
    
    return prime

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
print("The return list of only primes:", ret_onlyPrime(numbers))
