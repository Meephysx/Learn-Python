# Buatlah sebuah fungsi untuk mengurutkan sebuah string dalam urutan alfabetik.
# Contoh parameter: string = "python"
# Contoh output: "hnopty"

def alfabet(string):
    return ''.join(sorted(string))
string = "python"
print(alfabet(string))