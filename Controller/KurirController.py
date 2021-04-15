from flask import Flask, request, jsonify
from Model.KurirModel import KurirModel
from app import app, db

# List Semua Data Kurir
@app.route('/kurir', methods=['GET','POST'])
def Kurir():
    # Jika Method GET arahkan ke Pengambilan Data (View Semua Data)
    if request.method == 'GET':
        kurir = KurirModel.query.all()
        data = [
            {
                "Nip Kurir": kurirs.nip_kurir,
                "Nama Kurir": kurirs.nama_kurir,
                "Alamat Kurir": kurirs.alamat_kurir,
                "Tanggal Lahir Kurir": kurirs.tanggal_lahir_kurir

            } for kurirs in kurir
        ]
        return {
            "Status": 200,
            "Kurir": data
        }
    # Jika Method Post Arahkan Ke Insert
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            insert = KurirModel(
                nip_kurir=data['nip_kurir'],
                nama_kurir=data['nama_kurir'],
                alamat_kurir=data['alamat_kurir'],
                tanggal_lahir_kurir=data['tanggal_lahir_kurir']
            )
            db.session.add(insert)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data Kurir Berhasil Ditambahkan",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data Kurir Gagal Ditambahkan"
            }

@app.route('/kurir/<kurir_id>', methods=['GET','PUT','DELETE'])
def KurirById(kurir_id):
    # Ambil Data Sesuai ID
    kurirs = KurirModel.query.get_or_404(kurir_id)

    # Method GET Arahkan ke View Data By ID nya
    if request.method == 'GET':
        kurir = {
            "Nip Kurir": kurirs.nip_kurir,
            "Nama Kurir": kurirs.nama_kurir,
            "Alamat Kurir": kurirs.alamat_kurir,
            "Tanggal Lahir Kurir": kurirs.tanggal_lahir_kurir
        }
        return {
            "Status" : 200,
            "Kurir" : kurir
        }
    # Jika Method PUT Update Data
    elif request.method == 'PUT':
        if request.is_json:
            data = request.get_json()
            kurirs.nip_kurir = data['nip_kurir'],
            kurirs.nama_kurir = data['nama_kurir'],
            kurirs.alamat_kurir = data['alamat_kurir'],
            kurirs.tanggal_lahir_kurir = data['tanggal_lahir_kurir']
            db.session.add(kurirs)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data Kurir Berhasil Diubah",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data Kurir Gagal Diubah"
            }
    elif request.method == 'DELETE':
        db.session.delete(kurirs)
        db.session.commit()
        return {
            "Status": 200,
            "Message": "Data Kurir Berhasil Dihapus",
        }



