# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:26:16 2021

@author: joi
laporan ke 2
"""

from math import sin, cos, sqrt, atan2, radians

x = input('Selamat Datang, dengan siapa disini?: ')
print('Selamat Datang', x,'Untuk memulai sistem, silahkan ketik "Mulai" jika tidak silahkan ketik "Tidak"')
which = input('Tentukan pilihanmu: ')

if which == 'Mulai' :
    lat1 = radians(float(input('Masukkan Lattitude kota : ')))
    long1 = radians(float(input('Masukkan Longitude kota : ')))
    lat2 = radians(float(input('Masukkan Lattitude kota : ')))
    long2 = radians(float(input('Masukkan Longitude kota : ')))

    longmin = (long2 - long1)
    latmin = (lat2 - lat1)

    R = 6373.0
    a = sin(latmin / 2)**2 + cos(lat1) * cos(lat2) * sin(longmin / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print('Jarak antara dua titik kota adalah', distance, 'Km')
    print('Terima Kasih')
    
elif which == 'Tidak' :
    print('Terima Kasih')
    
else :
    print('Mohon Maaf, silahkan masukkan kata yang benar !')
