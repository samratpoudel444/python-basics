text= input("Enter a string: ")
text= text.lower()
words= text.split()

count= 0
for word in words:
    for char in word:
    if(word == "a" or word == "e" or word == "i" or word == "o" or word == "u" ):
    count += 1

print("Total no of vowels are: ", count)