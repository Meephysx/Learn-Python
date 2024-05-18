# Buatlah sebuah fungsi untuk mengecek apakah sebuah string adalah palindrom atau tidak.
# Contoh parameter: kata = "level"
# Contoh output: "level adalah palindrom"

def cek_palindrom(x):
    x = x.lower()

    if x == x[::-1]:
        return f"{x} adalah palindrom"
    else:
        f"{x} bukan palindrom"
print(cek_palindrom ("level"))