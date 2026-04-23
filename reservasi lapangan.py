class Lapangan:
    def __init__(self, nama, harga_sewa):
        self.nama = nama
        self.harga_sewa = harga_sewa
        self.jadwal_terisi = []

    def cek_jadwal(self, jam):
        return jam not in self.jadwal_terisi


class Member:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo


class Resepsionis:
    def __init__(self, nama):
        self.nama = nama

class Resepsionis:
    def __init__(self, nama):
        self.nama = nama

    def proses_booking(self, member, lapangan, jam):

        if not lapangan.cek_jadwal(jam):
            print("❌ Jadwal sudah terisi")
            return False

        if member.saldo < lapangan.harga_sewa:
            print("❌ Saldo tidak cukup")
            return False

        member.saldo -= lapangan.harga_sewa
        lapangan.jadwal_terisi.append(jam)

        print("✅ Booking berhasil")
        return True

class Lapangan:
    def __init__(self, nama, harga_sewa):
        self.__nama = nama
        self.__harga_sewa = harga_sewa
        self.__jadwal_terisi = []

    def cek_jadwal(self, jam):
        return jam not in self.__jadwal_terisi

    def tambah_jadwal(self, jam):
        self.__jadwal_terisi.append(jam)

    def get_harga(self):
        return self.__harga_sewa


class Member:
    def __init__(self, nama, saldo):
        self.__nama = nama
        self.__saldo = saldo

    def get_nama(self):
        return self.__nama

    def get_saldo(self):
        return self.__saldo

    def kurangi_saldo(self, jumlah):
        self.__saldo -= jumlah


class Resepsionis:
    def __init__(self, nama):
        self.__nama = nama

    def proses_booking(self, member, lapangan, jam):
        print(f"\n{member.get_nama()} mencoba booking jam {jam}")

        # VALIDASI JAM
        if jam < 0 or jam > 24:
            print("❌ Jam tidak valid")
            return False

        # VALIDASI JADWAL
        if not lapangan.cek_jadwal(jam):
            print("❌ Jadwal sudah terisi")
            return False

        # VALIDASI SALDO
        if member.get_saldo() < lapangan.get_harga():
            print("❌ Saldo tidak cukup")
            return False

        # PROSES BOOKING
        member.kurangi_saldo(lapangan.get_harga())
        lapangan.tambah_jadwal(jam)

        print("✅ Booking berhasil")
        print(f"Sisa saldo: {member.get_saldo()}")
        return True


# =========================
# SIMULASI
# =========================

lapangan = Lapangan("Futsal A", 50000)
member1 = Member("Andi", 100000)
member2 = Member("Budi", 10000)
admin = Resepsionis("Siti")

print("=== SIMULASI SUKSES ===")
admin.proses_booking(member1, lapangan, 10)

print("\n=== SIMULASI GAGAL ===")

# Gagal karena jadwal bentrok
admin.proses_booking(member1, lapangan, 10)

# Gagal karena saldo kurang
admin.proses_booking(member2, lapangan, 12)

# Gagal karena jam tidak valid
admin.proses_booking(member1, lapangan, 30)