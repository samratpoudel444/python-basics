def is_anagram(str1, str2):
    if sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower()):
        return True
    else:
        return False
        

print(is_anagram("samrat","ratsam"))