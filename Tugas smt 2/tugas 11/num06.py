# Tuliskan sebuah fungsi untuk menghitung jumlah kata dalam sebuah kalimat.
# Contoh parameter: kalimat = "Ini adalah contoh kalimat"

def hitungKata(s:str):
    s_list = s.strip().split()
    return len(s_list)

print(hitungKata("Ini adalah contoh kalimat"))