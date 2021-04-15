import numpy as np
from scipy import spatial
from geopy.distance import distance as geodist
import json,urllib.request

class ACOTSP :
    def __init__(self,
                 fungsi,
                 jumlah_tujuan,
                 jumlah_semut,
                 batas_literasi,
                 matriks_tujuan,
                 alpha,
                 beta,
                 rho,
                 phenorome_awal=None):

        # Inisialisasi Variabel
        self.fungsi = fungsi
        self.jumlah_tujuan = jumlah_tujuan
        self.jumlah_semut = jumlah_semut
        self.batas_literasi = batas_literasi
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.phenorome_awal = phenorome_awal

        # Variabel Mencari Invers Jarak
        self.invers_jarak = 1 / (matriks_tujuan + 1e-10 * np.eye(jumlah_tujuan, jumlah_tujuan))

        # Variabel Nilai dari Tau diberi 1 (Phenorome Awal)
        if self.phenorome_awal == None:
            self.Tau = np.ones((jumlah_tujuan, jumlah_tujuan))
        else:
            self.Tau = np.full((jumlah_tujuan, jumlah_tujuan), self.phenorome_awal)

        # Variabel Jalur Perayapan Semut
        self.Perayapan = np.zeros((jumlah_semut, jumlah_tujuan)).astype(np.int64)

        # Variabel Jarak Jelajah Semut
        self.y = None

        # Variabel Menulis Rute Terbaik
        self.generasi_terbaik_x, self.generasi_terbaik_y = [], []

        # Variabel Mencatat History Jejak Terbaik
        self.history_terbaik_x, self.history_terbaik_y = self.generasi_terbaik_x, self.generasi_terbaik_y

        # Variabel Rute Terbaik X, Y
        self.terbaik_x, self.terbaik_y = None, None

    def run(self, batas_literasi = None):
        # Cek Nilai Batas Literasi
        self.batas_literasi = batas_literasi or self.batas_literasi

        # Perulangan Literasi
        for i in range(self.batas_literasi):
            probabilitas_matrix = (self.Tau ** self.alpha) * (self.invers_jarak) ** self.beta
            # Perulangan Semut
            for j in range(self.jumlah_semut):
                self.Perayapan[j, 0] = 0
                # Perulangan Tujuan
                for k in range(self.jumlah_tujuan - 1):
                    # Inisialisasi Tabu List Rute
                    tabulist_set = set(self.Perayapan[j, :k + 1])
                    tabulist_terisi = list(set(range(self.jumlah_tujuan)) - tabulist_set)
                    # Hitung Probabilitas Semua Semut
                    probabilitas = probabilitas_matrix[self.Perayapan[j, i], tabulist_terisi]
                    probabilitas = probabilitas / probabilitas.sum()
                    point_selanjutnya = np.random.choice(tabulist_terisi, size=1, p=probabilitas)[0]
                    self.Perayapan[j, k + 1] = point_selanjutnya

            # kalkulasi jarak rute
            y = np.array([self.fungsi(i) for i in self.Perayapan])

            # catat rute terbaik
            index_terbaik = y.argmin()
            x_terbaik, y_terbaik = self.Perayapan[index_terbaik, :].copy(), y[index_terbaik].copy()
            self.generasi_terbaik_x.append(x_terbaik)
            self.generasi_terbaik_y.append(y_terbaik)

            # Hitung phenerome lokal untuk literasi selanjutnya
            delta_tau = np.zeros((self.jumlah_tujuan, self.jumlah_tujuan))
            for j in range(self.jumlah_semut):
                for k in range(self.jumlah_tujuan - 1):
                    n1, n2 = self.Perayapan[j, k], self.Perayapan[j, k + 1]
                    delta_tau[n1, n2] += 1 / y[j]
                n1, n2 = self.Perayapan[j, self.jumlah_tujuan - 1], self.Perayapan[j, 0]
                delta_tau[n1, n2] += 1 / y[j]

            # hitung phenorome global jika literasi sudah habis
            self.Tau = (1 - self.rho) * self.Tau + delta_tau

        generasi_terbaik = np.array(self.generasi_terbaik_y).argmin()
        self.terbaik_x = self.generasi_terbaik_x[generasi_terbaik]
        self.terbaik_y = self.generasi_terbaik_y[generasi_terbaik]
        return self.terbaik_x, self.terbaik_y, self.Perayapan