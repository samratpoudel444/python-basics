number= int(input("enter the no of Element"))

for i in range(0, number):
    a[i]= int(input(f"Enter "{i} "th Element"))
    a.append(element)

sum =0
for num in a:
    sum= sum + num
print("The total sum of list is", sum)