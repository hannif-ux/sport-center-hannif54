from datetime import datetime

class Lapangan:
    def __init__(self, nama, harga_sewa):
        self.nama = nama
        self.harga_sewa = harga_sewa
        self.jadwal_terisi = []  # Menyimpan jam yang sudah di-booking (misal: 10, 11, 14)

    def cek_jadwal(self, jam):
        return jam not in self.jadwal_terisi


class Member:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo


class Resepsionis:
    def __init__(self, nama):
        self.nama = nama

    def proses_booking(self, member, lapangan, jam):
        print(f"\n--- Sesi Reservasi oleh {self.nama} ---")

        # Aturan Bisnis 1: Cek Bentrok Jadwal
        if not lapangan.cek_jadwal(jam):
            print(f"Gagal: Jadwal lapangan {lapangan.nama} jam {jam}:00 sudah penuh (bentrok)!")
            return False

        # Aturan Bisnis 2: Cek Saldo Member
        if member.saldo < lapangan.harga_sewa:
            print(f"Gagal: Saldo {member.nama} tidak mencukupi! (Saldo: {member.saldo}, Harga: {lapangan.harga_sewa})")
            return False

        # Jika lolos semua aturan
        member.saldo -= lapangan.harga_sewa
        lapangan.jadwal_terisi.append(jam)
        print(f"Berhasil! {member.nama} telah membooking {lapangan.nama} untuk jam {jam}:00.")
        print(f"Sisa Saldo {member.nama}: Rp{member.saldo}")
        return True


# --- Simulasi Penggunaan Aplikasi ---

# 1. Inisialisasi Data (Entitas)
lapangan_futsal = Lapangan("Futsal A", 50000)
member_1 = Member("Andi", 100000)
member_2 = Member("Budi", 30000)
staf_admin = Resepsionis("Siti")

# 2. Percobaan Booking Berhasil
staf_admin.proses_booking(member_1, lapangan_futsal, 10)

# 3. Percobaan Booking Gagal (Jadwal Bentrok)
staf_admin.proses_booking(member_2, lapangan_futsal, 10)

# 4. Percobaan Booking Gagal (Saldo Kurang)
staf_admin.proses_booking(member_2, lapangan_futsal, 15)