
def count_frequency(data):
    count={}
    for i in data:
        if(i in count):
            count[i] += 1
        else:
            count[i]=1
    return count

data=["apple", "banana","apple", "banana", "banana",  ]
print(count_frequency(data))