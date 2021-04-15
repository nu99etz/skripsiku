from app import db
import os

class KurirModel(db.Model):
    __tablename__ = 'kurir'
    id = db.Column(db.Integer, primary_key=True)
    nip_kurir = db.Column(db.String(15))
    nama_kurir = db.Column(db.String(255))
    alamat_kurir = db.Column(db.String(255))
    tanggal_lahir_kurir = db.Column(db.String(20))
    is_aktif = db.Column(db.Integer, default=1)

    def __init__(self, nip_kurir, nama_kurir, alamat_kurir, tanggal_lahir_kurir):
        self.nip_kurir = nip_kurir
        self.nama_kurir = nama_kurir
        self.alamat_kurir = alamat_kurir
        self.tanggal_lahir_kurir = tanggal_lahir_kurir,
        # self.is_aktif = is_aktif