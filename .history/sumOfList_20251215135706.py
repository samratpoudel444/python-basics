number = int(input("Enter the number of elements: "))

a = [] 

for i in range(number):
    element = int(input(f"Enter {i+1}th element: "))
    a.append(element)  # add to list

# Calculate sum
total = 0
for num in a:
    total += num

print("The total sum of the list is:", total)
