from flask import Flask, request, jsonify
from Model.PengirimanModel import PengirimanModel
import numpy as np
from scipy import spatial
from geopy.distance import distance as geodist
import json
from Library.ACOTSP import ACOTSP
from app import app, db

# ACO Penghitungan
@app.route('/aco-tsp', methods=['POST'])
def ACOTSPHitung():
    if request.method == 'POST':
        if request.is_json:
            post = request.get_json()
            semut = post['jumlah_semut']
            literasi = post['batas_literasi']
            alpha = post['alpha']
            beta = post['beta']
            rho = post['rho']
            phenorome_awal = post['phenorome_awal']
            pengiriman = PengirimanModel.query.all()
            data = [
                {
                    "Longitude": kirim.longitude,
                    "Lattitude": kirim.lattitude

                } for kirim in pengiriman
            ]

            json_obj = {
                "Status": 200,
                "Pengiriman": data,
                "Total": len(data)
            }

            value = []
            for key in json_obj["Pengiriman"]:
                value.append([key["Lattitude"], key["Longitude"]])

            nodes = np.array(value)
            num_points = len(nodes)
            distance_matrix = spatial.distance.cdist(nodes, nodes, lambda u, v: geodist(u, v).kilometers)

            def cal_total_distance(routine):
                num_points, = routine.shape
                return (sum(
                    [distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in
                     range(num_points)]))

            aca = ACOTSP(fungsi=cal_total_distance, jumlah_tujuan=num_points,
                         jumlah_semut=semut, batas_literasi=literasi,
                         matriks_tujuan=distance_matrix, alpha=alpha, beta=beta, rho=rho,
                         phenorome_awal=phenorome_awal)
            best_x, best_y, perayapan = aca.run()

            def Coordinates(id):
                koordinates = PengirimanModel.query.filter_by(id_pengiriman = id).first()
                return {
                    'id_pengiriman' : id,
                    'lat' : koordinates.lattitude,
                    'long' : koordinates.longitude,
                    'alamat' : koordinates.alamat_pengiriman
                }

            array_koordinate = []
            array_rute = []
            for i in best_x:
                # array_koordinate.append(i)
                koord = Coordinates(str(i))
                array_rute.append(koord)

            # stringjoin = ",".join(map(str, array_koordinate))

            obj = {
                "Status" : 200,
                "Rute" : array_rute,
                # "Koordinat": array_rute,
                "Jarak": best_y
            }

            return obj

