# -*- coding: utf-8 -*-
"""Program Transformasi 3D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aH79HFrBHsC_d5YBNsjMLa96iFbsrlcz
"""

###################################
# Program Transformasi 3D
# Anggota Kelompok:
# 1. Anas Syahirul Alim
#    NIM: 19/439809/TK/48539
# 2. Roby Attoillah
#    NIM: 19/444068/TK/49264
# 3. T Rafi N M
#    NIM: 19/439823/TK/48553
####################################

# Import library yang dibutuhkan
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_t(m):  # Plot ke bidang 2D
    x, y, z=zip(*np.transpose(m))    # Memisahkan tiap kolom matriks m menjadi komponen x, y dan z
    t1, t2, t3, t4, t5 = zip(*m)    # Memisahkan matriks m menjadi 5 titik (x, y, z)
    sisi = [[t1, t2, t5], [t1, t4, t5], [t3, t2, t5], [t3, t4, t5], [t1, t2, t3, t4]]   # Array sisi yang dibentuk oleh tiga titik

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Membuat bidang 3D
    ax.scatter3D(x, y, z)   # Plot scatter titik x, y, dan z
    plot = Poly3DCollection(sisi, facecolors=[0.5, 0.5, 1], linewidths=1, edgecolors='r', alpha=.25)   # Plot sisi piramida
    ax.add_collection3d(plot)   # Plot sisi piramida
    plt.show()

def homogen_t(m):
    m = np.insert(m, 3, 1, axis=0)    # Menambahkan 1 baris pada matriks m (3x5) sehingga menjadi matriks (4x5) dengan nilai kolom 4 = 1
    return m

def translasi(m, t, i):
    if i==1: ## i=1, maka lakukan translasi biasa
        tx = int(input('Translasi ke arah x sebesar = '))
        ty = int(input('Translasi ke arah y sebesar = '))
        tz = int(input('Translasi ke arah z sebesar = '))
        trans = np.array([[1, 0, 0, tx],
                          [0, 1, 0, ty],
                          [0, 0, 1, tz],
                          [0, 0, 0, 1]])
        M = np.dot(trans, m)

    elif i==2: ## i=2 digunakan untuk keperluan rotasi terhadap sumbu x, jadi untuk pergeseran sumbu x saja
        trans = np.array([[1, 0, 0, -t],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        M = np.dot(m, trans)

    elif i==3: ## i=3 digunakan untuk keperluan rotasi terhadap sumbu y, jadi untuk pergeseran sumbu y saja
        trans = np.array([[1, 0, 0, 0],
                          [0, 1, 0, -t],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        M = np.dot(m, trans)

    elif i==4: ## i=2 digunakan untuk keperluan rotasi terhadap sumbu z, jadi untuk pergeseran sumbu z saja
        trans = np.array([[1, 0 ,0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, -t],
                          [0, 0, 0, 1]])
        M = np.dot(m, trans)

    return M

def scale(m):
    sx = float(input("Masukkan Skala Pembesaran x: "))
    sy = float(input("Masukkan Skala Pembesaran y: "))
    sz = float(input("Masukkan Skala Pembesaran z: "))
    m_sc = np.array([[sx, 0, 0, 0],
                    [0, sy, 0, 0],
                    [0, 0, sz, 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_sc, m)
    return M

def rotation_x(m):
    t = int(input('Rotasi terhadap x = '))
    m = translasi(m, t, 2) # ditranslasi sebanyak t ke arah kiri/-t(dinegatifkan saat di fungsi translasi), i=2

    d = np.radians(float(input("Masukkan sudut putar: ")))
    m_r = np.array([[1, 0, 0, 0],
                    [0, np.cos(d), -np.sin(d), 0],
                    [0, np.sin(d), np.cos(d), 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_r, m)
    M = translasi(M, -t, 2)
    return M

def rotation_y(m):
    t = int(input('Rotasi terhadap y ='))
    m = translasi(m, t, 3)
    d = np.radians(float(input("Masukkan sudut putar: ")))
    m_r = np.array([[1, 0, 0, 0],
                    [0, np.cos(d), -np.sin(d), 0],
                    [0, np.sin(d), np.cos(d), 0,],
                    [0, 0, 0, 1]])
    M = np.dot(m_r, m)
    M = translasi(M, -t, 3)
    return M

def rotation_z(m):
    t = int(input('Rotasi terhadap z = '))
    m = translasi(m, t, 4)
    d = np.radians(float(input("Masukkan sudut putar: ")))
    m_r = np.array([[np.cos(d), -np.sin(d), 0, 0],
                    [np.sin(d), np.cos(d), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_r, m)
    M = translasi(M, -t, 4)
    return M

def shear_xy(m):
    sx = float(input("Masukkan Skala Shearing sumbu x: "))
    sy = float(input("Masukkan Skala Shearing sumbur y: "))
    m_s = np.array([[1, 0, sx, 0],
                    [0, 1, sy, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_s, m)
    return M

def shear_yz(m):
    sy = float(input("Masukkan Skala Shearing sumbu y: "))
    sz = float(input("Masukkan Skala Shearing sumbu z: "))
    m_s = np.array([[1, 0, 0, 0],
                    [0, sy, 0, 0],
                    [0, sz, 1, 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_s, m)
    return M

def shear_xz(m):
    sx = float(input("Masukkan Skala Shearing sumbu y: "))
    sz = float(input("Masukkan Skala Shearing sumbu z: "))
    m_s = np.array([[sx, 0, 0, 0],
                    [0, 1, 0, 0],
                    [sz, 0, 1, 0],
                    [0, 0, 0, 1]])
    M = np.dot(m_s, m)
    return M

def operasi(pil, m):
    # Mengembalikan nilai matriks transformasi (mt)
    if pil==1:
        mt = translasi(m, 0, 1)
        return mt
    elif pil==2:
        mt = scale(m)
        return mt
    elif pil==3:
        mt = rotation_x(m)
        return mt
    elif pil==4:
        mt = rotation_y(m)
        return mt
    elif pil==5:
        mt = rotation_z(m)
        return mt
    elif pil==6:
        mt = shear_xy(m)
        return mt
    elif pil==7:
        mt = shear_yz(m)
        return mt
    elif pil==8:
        mt = shear_xz(m)
        return mt
    else:
        txt = 'Pilih nomor yang tersedia!'
        return txt

print("Program ini merupakan program untuk menghitung Transformasi bangun Geometri 3D")
print("Bangun geometri yang dipilih: Piramida\nInput: 5 titik\n")
print('======= Program dibuat oleh ===========')
print('1. Anas Syahirul Alim     [19/439809/TK/48539]')
print('2. Roby Attoillah         [19/444068/TK/49264]')
print('3. Tengku Rafi Nugroho M  [19/439823/TK/48553]')
print("======= Panduan input titik geometri =======")
print("1. Terdapat 5 input titik x y z")
print("2. Input terlebih dahulu 4 titik sebagai alas piramida")
print("3. Input 1 titik terakhir sebagai puncak piramida")
print("Contoh input:")
print("titik 1 (x,y,z): -1 -1 -1")
print("titik 2 (x,y,z): 1 -1 -1")
print("titik 3 (x,y,z): 1 1 -1")
print("titik 4 (x,y,z): -1 1 -1")
print("titik 5 (x,y,z): 0 0 3")
print("============================================\n")

m=np.zeros((3,5))   # membuat matriks nol 3x5 untuk diisi titik-titik koordinat

for i in range(0,5):    # Iterasi untuk mendapatkan user input
    x, y, z= map(float, input("Input x(spasi)y(spasi)z: ").split())    # Mapping input user ke variabel x, y dan z
    m[:,i]+=[x,y,z]  # x, y, dan z dimasukkan ke kolom i matriks m

print("\nMatriks input:\n", m)
plot_t(m) # plot m

mh = homogen_t(m)  # Membuat matriks menjadi homogen

print("\nSilahkan pilih jenis transformasi pada piramida yang telah ditentukan")
print('1. Translasi')
print('2. Scaling')
print('3. Rotasi terhadap sumbu x')
print('4. Rotasi terhadap sumbu y')
print('5. Rotasi terhadap sumbu z')
print('6. Shearing pada sumbu xy')
print('7. Shearing pada sumbu yz')
print('8. Shearing pada sumbu xz')

mt = np.eye(4)  # Membuat matriks identitas 4x4 untuk operasi matriks transformasi
iterasi=True

while (iterasi):   # Iterasi untuk membuat matriks transformasi komposit
    pil = int(input("\nPilih transformasi: "))
    mt = operasi(pil, mt)   # Membuat matriks transformasi komposit
    pil2 = input("\nLakukan transformasi lagi? (y/n) ")
    if pil2 == 'y':
        iterasi=True
    elif pil2== 'n':
        iterasi=False

print("\nMatriks Transformasi:\n", np.round(mt, 2))

ms = np.dot(mt, mh)     # dot product matriks transformasi dengan matriks homogen
m = np.delete(ms, 3, axis=0)  # Mengembalikan ke bentuk matriks 3x5 dengan mereduksi baris homogen
print("\nMatriks hasil transformasi:\n", m)
plot_t(m)

