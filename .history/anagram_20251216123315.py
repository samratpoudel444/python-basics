def is_anagram(str1, str2):
    if sorted(str1.replace(" ", "").lower() == sorted(str1.replace(" ", "")).lower()):
        return True

print(is_anagram("samrat","ratsam"))