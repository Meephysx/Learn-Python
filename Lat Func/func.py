# def my_hello():
#     print("Hello, World")
# my_hello()

# def hitung(a, b):
#     hasil = a * b
#     return hasil
# print(hitung(5, 5))

# Soal
noKTP = "3272070408040001"
tanggalLahir = noKTP[6:8]

namaBulan = ["January", "Februari", "Maret", "April", "Mei", "Juni", "July", "Agustus", "September", "Oktober", "November", "Desember"]
noBulan = noKTP[8:10]
bulanLahir = namaBulan[int(noBulan)-1]

tahunLahir = noKTP[10:12]
tahunLampau = "2004"
tahunSekarang = "2024"
newYear = tahunSekarang-tahunSekarang
compareYear = int(newYear[-2:])

print(f"TanggalLahir : {tanggalLahir}" )
print(f"bulanLahir : {bulanLahir} ")
print(f"tahunLahir : {compareYear} ")

# Tanggal Lahir = 04 Agustus 2004
# Umur Anda = 19 Tahun
# Zodiak = Leo

