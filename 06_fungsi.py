def hitung_nilai_akhir(tugas, uts, uas):
    return (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

def konversi_grade(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"

def tentukan_status(grade):
    if grade in ["A", "B", "C"]:
        return "LULUS"
    return "TIDAK LULUS"

def cetak_transkrip_ringkas(nama, tugas, uts, uas):
    akhir = hitung_nilai_akhir(tugas, uts, uas)
    grade = konversi_grade(akhir)
    status = tentukan_status(grade)

    print("==================================")
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {tugas}")
    print(f"Nilai UTS      : {uts}")
    print(f"Nilai UAS      : {uas}")
    print(f"Nilai Akhir    : {akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")
    print("==================================")

cetak_transkrip_ringkas("Budi Santoso", 85, 78, 90)
cetak_transkrip_ringkas("Siti Aminah", 60, 50, 45)
