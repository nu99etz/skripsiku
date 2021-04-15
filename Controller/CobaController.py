from flask import Flask, request, jsonify
from Model.LoginModel import LoginModel
from app import app, db

# List Semua Data Kurir
@app.route('/coba', methods=['GET','POST'])
def Coba():
    # Jika Method GET arahkan ke Pengambilan Data (View Semua Data)
    if request.method == 'GET':
        user = LoginModel.query.all()
        data = [
            {
                "ID" : users.id,
                "Username": users.username,
                "Password": users.password,

            } for users in user
        ]
        return {
            "Status": 200,
            "User": data
        }
    # Jika Method Post Arahkan Ke Insert
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            insert = LoginModel(
                username=data['username'],
                password=data['password'],
            )
            db.session.add(insert)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data User Berhasil Ditambahkan",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data User Gagal Ditambahkan"
            }

@app.route('/coba/<coba_id>', methods=['GET','PUT','DELETE'])
def CobaById(coba_id):
    # Ambil Data Sesuai ID
    users = LoginModel.query.get_or_404(coba_id)

    # Method GET Arahkan ke View Data By ID nya
    if request.method == 'GET':
        user = {
            "Username": users.username,
            "Password": users.password,
        }
        return {
            "Status" : 200,
            "User" : user
        }
    # Jika Method PUT Update Data
    elif request.method == 'PUT':
        if request.is_json:
            data = request.get_json()
            users.username = data['username'],
            users.password = data['password'],
            db.session.add(users)
            db.session.commit()
            return {
                "Status": 200,
                "Message": "Data User Berhasil Diubah",
            }
        else:
            return {
                "Status": 200,
                "Message": "Data User Gagal Diubah"
            }
    elif request.method == 'DELETE':
        db.session.delete(users)
        db.session.commit()
        return {
            "Status": 200,
            "Message": "Data Users Berhasil Dihapus",
        }



