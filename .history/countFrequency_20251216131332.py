
def count_frequency(data):
    count={}
    for i in data:
        if(i in count):
            i[num] += 1
        else:
            i[num]=1
    return count

data=["apple", "banana", ]
print(count_frequency(data))