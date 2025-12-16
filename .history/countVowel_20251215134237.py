text= input("Enter a string: ")

words= text.split()

count= int(0
for word in words:
    if(word == "a" or word == "e" or word == "i" or word == "o" or word == "u" ):
    count = count+1

print("Total no of vowels are: ", count)