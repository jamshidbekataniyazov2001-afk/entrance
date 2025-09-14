# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:23:13 2025

@author: user
"""
son = input("Istalgan butun son kiriting: ")
def kvadrat_kub(son):
    kvadrat = int(son)**2
    kub = int(son)**3

    return kvadrat,kub
print('bu sonning kvadrati va kubi mos ravishda', kvadrat_kub(son), 'ga teng')
    