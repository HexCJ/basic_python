mahasiswa = {
    "nim": "230101050",
    "nama": "Andi Pratama",
    "jurusan": "Teknik Informatika",
    "semester": 3,
    "matkul_diambil": ["Algoritma", "Basis Data", "Sistem Operasi"],
    "nilai_matkul": {
        "Algoritma": 85,
        "Basis Data": 78,
        "Sistem Operasi": 90
    }
}

print("=== AKSES DICTIONARY ===")
print("NIM     :", mahasiswa["nim"])
print("Nama    :", mahasiswa["nama"])
print("Jurusan :", mahasiswa["jurusan"])

print("\n=== MENAMBAH DAN MENGUBAH DATA ===")
mahasiswa["ipk"] = 3.65
mahasiswa["matkul_diambil"].append("Jaringan Komputer")
mahasiswa["nilai_matkul"]["Jaringan Komputer"] = 80

print("IPK Terkini:", mahasiswa["ipk"])
print("Matkul Terbaru:", mahasiswa["matkul_diambil"])

print("\n=== ITERASI KEY DAN VALUE PADA DICTIONARY ===")
for matkul, nilai in mahasiswa["nilai_matkul"].items():
    print(f"Mata Kuliah: {matkul:<20} | Nilai: {nilai}")

total_nilai = sum(mahasiswa["nilai_matkul"].values())
rata_nilai = total_nilai / len(mahasiswa["nilai_matkul"])
print(f"\nRata-rata Nilai: {rata_nilai:.2f}")
