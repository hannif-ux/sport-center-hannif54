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

        def proses_booking(self, member, lapangan, jam):
            if not lapangan.cek_jadwal(jam):
                print("Jadwal bentrok")
                return False

            if member.saldo < lapangan.harga_sewa:
                print("Saldo tidak cukup")
                return False

            member.saldo -= lapangan.harga_sewa
            lapangan.jadwal_terisi.append(jam)
            print("Booking berhasil")
            return True

lapangan = Lapangan("Futsal A", 50000)
member = Member("Andi", 100000)
admin = Resepsionis("Siti")

admin.proses_booking(member, lapangan, 10)