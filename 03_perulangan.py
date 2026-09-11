daftar_matkul = [
    "Struktur Data",
    "Basis Data",
    "Pemrograman Berorientasi Objek",
    "Jaringan Komputer",
    "Aljabar Linier"
]

print("=== PERULANGAN FOR (FOREACH LIST) ===")
for matkul in daftar_matkul:
    print("-", matkul)

print("\n=== PERULANGAN FOR DENGAN INDEX (ENUMERATE) ===")
for no, matkul in enumerate(daftar_matkul, start=1):
    print(f"{no}. {matkul}")

print("\n=== PERULANGAN FOR DENGAN RANGE ===")
for i in range(1, 6):
    print(f"Iterasi ke-{i}")

print("\n=== PERULANGAN WHILE ===")
hitung = 1
while hitung <= 5:
    print(f"Nilai counter: {hitung}")
    hitung += 1

print("\n=== BREAK DAN CONTINUE ===")
for angka in range(1, 11):
    if angka == 4:
        continue
    if angka == 8:
        break
    print("Angka:", angka)


buah = ["Apel", "Jeruk", "Mangga"]
for item in buah:
    print(item)