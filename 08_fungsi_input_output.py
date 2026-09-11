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

def cetak_transkrip_ringkas(nim, nama, semester, tugas, uts, uas):
    akhir = hitung_nilai_akhir(tugas, uts, uas)
    grade = konversi_grade(akhir)
    status = tentukan_status(grade)

    print("\n==================================")
    print("    TRANSKRIP NILAI MAHASISWA     ")
    print("==================================")
    print(f"NIM            : {nim}")
    print(f"Nama Mahasiswa : {nama}")
    print(f"Semester       : {semester}")
    print(f"Nilai Tugas    : {tugas:.2f}")
    print(f"Nilai UTS      : {uts:.2f}")
    print(f"Nilai UAS      : {uas:.2f}")
    print(f"Nilai Akhir    : {akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")
    print("==================================")

def input_data_mahasiswa():
    print("--- INPUT DATA MAHASISWA ---")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama Mahasiswa: ")
    semester = int(input("Masukkan Semester: "))
    tugas = float(input("Masukkan Nilai Tugas (0-100): "))
    uts = float(input("Masukkan Nilai UTS (0-100): "))
    uas = float(input("Masukkan Nilai UAS (0-100): "))
    return nim, nama, semester, tugas, uts, uas

nim, nama, semester, tugas, uts, uas = input_data_mahasiswa()
cetak_transkrip_ringkas(nim, nama, semester, tugas, uts, uas)
