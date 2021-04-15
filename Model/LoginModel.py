from app import db
from Model import KurirModel
import os

class LoginModel(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255))
    is_aktif = db.Column(db.Integer, default=1)

    def __init__(self, username, password):
        self.username = username
        self.password = password