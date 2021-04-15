from app import db
import os

class PengirimanModel(db.Model):
    __tablename__ = 'alamat_pengiriman'
    id = db.Column(db.Integer, primary_key=True)
    id_pengiriman = db.Column(db.String(30))
    alamat_pengiriman = db.Column(db.Text, nullable=False)
    coordinates = db.Column(db.Text, nullable=False)
    lattitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, id_pengiriman, alamat_pengiriman, lattitude, longitude):
        self.id_pengiriman = id_pengiriman
        self.alamat_pengiriman = alamat_pengiriman
        self.coordinates = "[" + lattitude + ", " + longitude + "]"
        self.lattitude = lattitude
        self.longitude = longitude