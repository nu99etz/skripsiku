from flask import Flask, request, jsonify
from Model.PengirimanModel import PengirimanModel
from app import app, db

# List Semua Data Pengiriman Kurir
@app.route('/pengiriman', methods=['GET','POST'])
def Pengiriman():
    # Jika Method GET arahkan ke Pengambilan Data (View Semua Data)
    if request.method == 'GET':
        pengiriman = PengirimanModel.query.all()
        data = [
            {
                "ID Pengiriman": kirim.id_pengiriman,
                "Alamat Kurir": kirim.alamat_pengiriman,
                "Koordinat": kirim.coordinates,
                "Longitude" : kirim.longitude,
                "Lattitude" : kirim.lattitude

            } for kirim in pengiriman
        ]
        return {
            "Status": 200,
            "Pengiriman": data
        }
    # Jika Method Post Arahkan Ke Insert
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            insert = PengirimanModel(
                id_pengiriman=data['id_pengiriman'],
                alamat_pengiriman=data['alamat_pengiriman'],
                longitude=data['longitude'],
                lattitude=data['lattitude']
            )
            db.session.add(insert)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data Pengiriman Berhasil Ditambahkan",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data Pengiriman Gagal Ditambahkan"
            }

@app.route('/pengiriman/<pengiriman_id>', methods=['GET','PUT','DELETE'])
def PengirimanById(pengiriman_id):
    # Ambil Data Sesuai ID
    kirim = PengirimanModel.query.get_or_404(pengiriman_id)

    # Method GET Arahkan ke View Data By ID nya
    if request.method == 'GET':
        pengiriman = {
            "ID Pengiriman": kirim.id_pengiriman,
            "Alamat Kurir": kirim.alamat_pengiriman,
            "Koordinat": kirim.coordinates,
            "Longitude" : kirim.longitude,
            "Lattitude" : kirim.lattitude
        }
        return {
            "Status": 200,
            "Kurir": pengiriman
        }
        # Jika Method PUT Update Data
    elif request.method == 'PUT':
        if request.is_json:
            data = request.get_json()
            kirim.id_pengiriman = data['id_pengiriman'],
            kirim.alamat_pengiriman = data['alamat_pengiriman'],
            kirim.longitude = data['longitude'],
            kirim.lattitude = data['lattitude']
            db.session.add(kirim)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data Pengiriman Berhasil Diubah",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data Pengiriman Gagal Diubah"
            }
    elif request.method == 'DELETE':
        db.session.delete(kirim)
        db.session.commit()
        return {
            "Status": 200,
            "Message": "Data Pengiriman Berhasil Dihapus",
        }




