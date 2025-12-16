def is_anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
