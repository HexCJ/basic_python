data_mahasiswa = [
    {"nim": "230101001", "nama": "Ahmad Fauzi", "nilai": 88},
    {"nim": "230101002", "nama": "Citra Lestari", "nilai": 72},
    {"nim": "230101003", "nama": "Dedi Kurniawan", "nilai": 58},
    {"nim": "230101004", "nama": "Eka Saputri", "nilai": 95},
    {"nim": "230101005", "nama": "Fajar Ramadhan", "nilai": 48}
]

def dapatkan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

def tampilkan_semua_data(list_mhs):
    print("\n" + "=" * 50)
    print(f"{'NIM':<12} | {'NAMA':<18} | {'NILAI':<6} | {'GRADE':<5}")
    print("-" * 50)
    for mhs in list_mhs:
        grade = dapatkan_grade(mhs["nilai"])
        print(f"{mhs['nim']:<12} | {mhs['nama']:<18} | {mhs['nilai']:<6} | {grade:<5}")
    print("=" * 50)

def cari_mahasiswa(list_mhs, nim_dicari):
    for mhs in list_mhs:
        if mhs["nim"] == nim_dicari:
            return mhs
    return None

def hitung_rekap(list_mhs):
    total = 0
    lulus = 0
    for mhs in list_mhs:
        total += mhs["nilai"]
        if mhs["nilai"] >= 55:
            lulus += 1
    rata_rata = total / len(list_mhs)
    tidak_lulus = len(list_mhs) - lulus
    return rata_rata, lulus, tidak_lulus

tampilkan_semua_data(data_mahasiswa)

rata_rata, total_lulus, total_gagal = hitung_rekap(data_mahasiswa)
print(f"Rata-rata Nilai Kelas : {rata_rata:.2f}")
print(f"Mahasiswa Lulus       : {total_lulus} orang")
print(f"Mahasiswa Tidak Lulus : {total_gagal} orang")

print("\n=== PENCARIAN MAHASISWA ===")
nim_target = "230101003"
hasil_cari = cari_mahasiswa(data_mahasiswa, nim_target)

if hasil_cari:
    print(f"Mahasiswa dengan NIM {nim_target} ditemukan:")
    print(f"Nama  : {hasil_cari['nama']}")
    print(f"Nilai : {hasil_cari['nilai']}")
    print(f"Grade : {dapatkan_grade(hasil_cari['nilai'])}")
else:
    print(f"Mahasiswa dengan NIM {nim_target} tidak ditemukan.")
