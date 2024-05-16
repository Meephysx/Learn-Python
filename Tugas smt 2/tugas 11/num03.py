# Batlah sebuah fungsi untuk menghitung keliling dan luas persegi panjang dengan menerima input panjang dan lebar.
# Contoh parameter: panjang = 5, lebar = 3
# Contoh output:
# luas 15, keliling 16

def hitung_keliling_luas(p,l):
    luas = p * l
    keliling = 2 * (p + l)
    return luas , keliling

print(hitung_keliling_luas(5 , 3))