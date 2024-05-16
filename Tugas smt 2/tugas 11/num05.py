# Buatlah sebuah fungsi untuk menghitung nilai faktorial dari sebuah bilangan bulat.
# Contoh parameter: n = 5
# Contoh output: 120

def faktorial(bilangan):
    if bilangan == 0:
        return 1
    else:
        return bilangan * faktorial (bilangan - 1)

print(faktorial(5)) 