# Tuliskan sebuah fungsi untuk menghitung jumlah elemen unik dalam sebuah daftar (list).
# Contoh parameter: my_list = [1, 2, 3, 3, 4, 4, 5]
# Contoh output: 5

def menghitung_unique(my_list):
    return len(set(my_list))
print(menghitung_unique([1,2,3,3,4,4,5]))