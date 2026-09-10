nim = input("Masukkan NIM: ")
nama = input("Masukkan nama mahasiswa: ")
semester = int(input("Masukkan semester saat ini (1-8): "))
kehadiran = int(input("Masukkan jumlah kehadiran hadir (dari total 16 pertemuan): "))
nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
nilai_uts = float(input("Masukkan nilai UTS (0-100): "))
nilai_uas = float(input("Masukkan nilai UAS (0-100): "))

nilai_akhir = (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.5 * nilai_uas)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
elif nilai_akhir >= 40:
    grade = "D"
else:
    grade = "E"

if kehadiran >= 12:
    status_kehadiran = "Memenuhi syarat ujian (>= 75%)"
    syarat_absen = True
else:
    status_kehadiran = "Tidak memenuhi syarat ujian (< 75%)"
    syarat_absen = False

if semester <= 2:
    kategori_semester = "Tahap Persiapan Bersama"
elif semester <= 6:
    kategori_semester = "Tahap Inti Kejuruan"
else:
    kategori_semester = "Tahap Tugas Akhir"

status_lulus = False
if grade in ["A", "B", "C"] and syarat_absen:
    status_lulus = True

print("\n=== HASIL EVALUASI AKADEMIK ===")
print("NIM               :", nim)
print("Nama Mahasiswa    :", nama)
print(f"Semester          : {semester} ({kategori_semester})")
print(f"Kehadiran         : {kehadiran} / 16 pertemuan")
print("Status Absensi    :", status_kehadiran)
print(f"Nilai Akhir       : {nilai_akhir:.2f}")
print("Grade             :", grade)

if status_lulus:
    if nilai_akhir >= 85:
        print("Keterangan        : Lulus dengan predikat Pujian")
    else:
        print("Keterangan        : Lulus")
else:
    print("Keterangan        : Tidak Lulus (Wajib Mengulang)")
