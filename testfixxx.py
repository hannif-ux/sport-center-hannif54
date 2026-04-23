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