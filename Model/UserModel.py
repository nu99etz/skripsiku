from app import db
from Model import KurirModel
import os

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    nama_pengguna = db.Column(db.Integer, db.ForeignKey('kurir.id'), nullable=False)
    password = db.Column(db.String(255))
    is_aktif = db.Column(db.Integer, default=1)

    def __init__(self, username, nama_pengguna, password, is_aktif):
        self.username = username
        self.nama_pengguna = nama_pengguna
        self.password = password
        self.is_aktif = is_aktif