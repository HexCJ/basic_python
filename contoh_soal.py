print("Nama: ", nama)
print("Umur: ", umur)
print("Kategori: ", kategori)

nama = input("Masukkan Nama : ")
umur = int(input("Masukkan Umur : "))

if umur < 6:
    kategori = "Balita"

elif 6 <= umur <= 12: #ini untuk penggunaan rentang tanpa gunain operator dan (sama aja kayak menggunakan seperti ini: elif umur >= 6 and umur <= 12:)
    kategori = "Anak-anak"

elif 13 <= umur < 18:
    kategori = "Remaja"

elif 18 <= umur < 60:
    kategori = "Dewasa"

elif umur >= 60:
    kategori = "Lansia"

else:
    kategori = "Mohon input umur yang valid"

print("Nama:", nama)
print("Umur:", umur)
print("Kategori:", kategori)