daftar_nilai = [78, 90, 65, 88, 55, 92, 70, 60, 84, 45]

total_nilai = 0
nilai_tertinggi = daftar_nilai[0]
nilai_terendah = daftar_nilai[0]
jumlah_lulus = 0
jumlah_tidak_lulus = 0

for nilai in daftar_nilai:
    total_nilai += nilai

    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai

    if nilai < nilai_terendah:
        nilai_terendah = nilai

    if nilai >= 60:
        jumlah_lulus += 1
    else:
        jumlah_tidak_lulus += 1

rata_rata = total_nilai / len(daftar_nilai)

print("=== STATISTIK NILAI KELAS ===")
print("Daftar Nilai       :", daftar_nilai)
print(f"Total Nilai        : {total_nilai}")
print(f"Rata-rata Kelas    : {rata_rata:.2f}")
print(f"Nilai Tertinggi    : {nilai_tertinggi}")
print(f"Nilai Terendah     : {nilai_terendah}")
print(f"Jumlah Mahasiswa Lulus      : {jumlah_lulus}")
print(f"Jumlah Mahasiswa Tidak Lulus: {jumlah_tidak_lulus}")

print("\n=== DAFTAR NILAI DI ATAS RATA-RATA ===")
for nilai in daftar_nilai:
    if nilai > rata_rata:
        print(f"Nilai {nilai} (Di atas rata-rata)")
