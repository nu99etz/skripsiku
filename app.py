from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Inisialisasi APlikasi
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sapi@localhost/acotsp'
# Inisialisasi DB
db = SQLAlchemy(app)
# inisialisasi Migrate
migrate = Migrate(app, db)


basedir = os.path.abspath(os.path.dirname(__file__))
from Model import LoginModel
from Controller import KurirController, PengirimanController, ACOController, UIController, CobaController

if __name__ == '__main__':
    app.run(debug=True)