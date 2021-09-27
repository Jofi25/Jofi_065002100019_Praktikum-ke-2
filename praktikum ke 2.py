# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:19:46 2021

@author: jofi
"""

a = int(input('Masukkan nilai a = '))
b = int(input('Masukkan nilai b = '))

jumlah = a + b
print('Hasil dari', a, 'ditambah', b, '=', jumlah)
kurang = a - b
print('Hasil dari', a, 'dikurang', b, '=', kurang)
kali = a * b
print('Hasil dari', a, 'dikali', b, '=', kali)
sisa_bagi = a % b
print('Sisa bagi dari', a, 'dengan', b, '=', sisa_bagi)
bagi = a/b
print('Hasil dari', a, 'dibagi', b, '=', bagi)
import math
loga = math.log10(a)
print('Hasil dari log', a, '=', loga)
pangkat = a ** b
print('Hasil dari', a, 'pangkat', b, '=', pangkat)

