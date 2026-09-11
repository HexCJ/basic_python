print("=== MENU SISTEM AKADEMIK KAMPUS ===")
print("1. Lihat Jadwal Kuliah")
print("2. Isi Kartu Rencana Studi (KRS)")
print("3. Cetak Kartu Hasil Studi (KHS)")
print("4. Pengajuan Cuti Akademik")
print("5. Keluar")

pilihan = int(input("\nMasukkan pilihan menu (1-5): "))

match pilihan:
    case 1:
        print("Menu 1: Menampilkan jadwal kuliah semester ini.")
    case 2:
        print("Menu 2: Membuka formulir pengisian KRS.")
    case 3:
        print("Menu 3: Mengunduh Kartu Hasil Studi (KHS).")
    case 4:
        print("Menu 4: Membuka permohonan pengajuan cuti akademik.")
    case 5:
        print("Keluar dari sistem akademik.")
    case _:
        print("Pilihan tidak valid! Silakan pilih nomor 1 sampai 5.")

kode_hari = input("\nMasukkan singkatan hari (SEN/SEL/RAB/KAM/JUM/SAB/MIN): ").upper()

match kode_hari:
    case "SEN":
        kegiatan = "Senin: Kuliah Basis Data"
    case "SEL":
        kegiatan = "Selasa: Praktikum Jaringan Komputer"
    case "RAB":
        kegiatan = "Rabu: Kuliah Struktur Data"
    case "KAM":
        kegiatan = "Kamis: Kuliah Pemrograman Berorientasi Objek"
    case "JUM":
        kegiatan = "Jumat: Kuliah Aljabar Linier"
    case "SAB" | "MIN":
        kegiatan = "Sabtu / Minggu: Libur Akhir Pekan"
    case _:
        kegiatan = "Kode hari tidak dikenal."

print(kegiatan)
