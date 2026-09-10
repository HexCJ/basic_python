ipk_semester_lalu = float(input("Masukkan IPK semester lalu (0.00 - 4.00): "))
golongan_ukt = int(input("Masukkan golongan UKT (1 - 5): "))
status_tunggakan = input("Apakah ada tunggakan pembayaran? (y/t): ")

if ipk_semester_lalu >= 3.50:
    batas_sks = 24
elif ipk_semester_lalu >= 3.00:
    batas_sks = 22
elif ipk_semester_lalu >= 2.50:
    batas_sks = 20
elif ipk_semester_lalu >= 2.00:
    batas_sks = 18
else:
    batas_sks = 15

if golongan_ukt == 1:
    biaya_ukt = 500000
elif golongan_ukt == 2:
    biaya_ukt = 1000000
elif golongan_ukt == 3:
    biaya_ukt = 2500000
elif golongan_ukt == 4:
    biaya_ukt = 4000000
else:
    biaya_ukt = 6000000

ada_tunggakan = status_tunggakan.lower() == "y"

print("\n=== DATA AKADEMIK MAHASISWA ===")
print(f"IPK Semester Lalu   : {ipk_semester_lalu:.2f}")
print(f"Batas Maksimal SKS  : {batas_sks} SKS")
print(f"Golongan UKT        : Golongan {golongan_ukt}")
print(f"Tagihan UKT         : Rp {biaya_ukt:,}")

if not ada_tunggakan:
    print("Status Pengisian KRS: Diizinkan mengisi KRS")
else:
    print("Status Pengisian KRS: Ditolak, lunasi tunggakan terlebih dahulu")
