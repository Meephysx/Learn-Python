# Buatlah sebuah fungsi untuk menentukan apakah suatu kata adalah anagram atau tidak.
# Contoh parameter: kata1 = "listen", kata2 = "silent"
# Contoh output: True

def anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(anagram('listen', 'silent'))