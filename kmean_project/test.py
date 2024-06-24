import numpy as np
from random import randint
import math
 
def khoi_tao_cum(X, k):
    chi_so = np.random.choice(X.shape[0], k, replace = False)
    return X[chi_so]
 
def tinh_khoang_cach(X, cum):
    khoang_cach = np.zeros((X.shape[0], cum.shape[0]))
    for i in range(cum.shape[0]):
        for j in range(X.shape[0]):
            khoang_cach[j, i] = np.sqrt(np.sum((X[j] - cum[i])**2))
    return khoang_cach
 
def gan_cum(khoang_cach):
    nhan = []
    for kc in khoang_cach:
        nhan_gan_nhat = 0
        kc_nho_nhat = kc[0]
        for i in range(1, len(kc)):
            if kc[i] < kc_nho_nhat:
                kc_nho_nhat = kc[i]
                nhan_gan_nhat = i
        nhan.append(nhan_gan_nhat)
    return np.array(nhan)
 
def cap_nhat_cum(X, nhan, k):
    cum = np.zeros((k, X.shape[1]))
    for i in range(k):
        diem = X[nhan == i]
        if diem.shape[0] > 0:
            chi_so_ngau_nhien = np.random.choice(diem.shape[0])
            cum[i] = diem[chi_so_ngau_nhien]
    return cum
 
def kmeans(X, k, so_vong_lap_toi_da=100, nguong_dung=1e-4):
    cum = khoi_tao_cum(X, k)
    so_vong_lap = 0
    while so_vong_lap < so_vong_lap_toi_da:
        cum_cu = cum.copy()
        khoang_cach = tinh_khoang_cach(X, cum)
        nhan = gan_cum(khoang_cach)
        cum = cap_nhat_cum(X, nhan, k)
        if np.all(np.abs(cum - cum_cu) < nguong_dung):
            break
        so_vong_lap += 1
    return cum, nhan
 
def main():
    np.random.seed(42)
    X = np.vstack((np.random.randn(100, 2) + np.array([5, 5]),
                   np.random.randn(100, 2) + np.array([-5, -5]),
                   np.random.randn(100, 2) + np.array([5, -5])))
 
    k = 3
    cum, nhan = kmeans(X, k)
    print("Centroids (Tâm cụm):\n", cum)
    print("Labels (Nhãn):\n", nhan)
 
main()