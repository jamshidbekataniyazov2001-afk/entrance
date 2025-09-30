# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 06:33:27 2025

@author: user
"""

kitoblar =[]
kitob = "Yaxshi ko'rgan kitobingizni kiriting: "
ishora = True
while ishora:
    qiymat = input(kitob)
    kitoblar.append(qiymat)
    if qiymat == 'stop':
        ishora = False
    else:
        print(qiymat)
print ("Raxmat bilib oldim")
print(kitoblar)
