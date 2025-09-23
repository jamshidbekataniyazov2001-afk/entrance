# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 05:24:58 2025

@author: user
"""

import random
from uzwords import words

def soz_top():
   
    soz = random.choice(words)
    while '-' in words or ' ' in words:
        soz = random.choice(words)
    return soz.upper()
def yangi(eski_harf,soz):
    yangi_harf = ""
    for harf in soz:
        if harf in eski_harf:
            yangi_harf += harf
        else:
            yangi_harf += "-"
    return yangi_harf

def play():
    soz = soz_top()
    soz_harflari = set(soz)
    eski_harf = ""
    print(f"Men {len(soz)} xonali soz o'yladim topingchi")
    while soz_harflari:
        print(yangi(eski_harf,soz))
        if eski_harf:
            print(f"Kiritgan harflaringiz: {eski_harf}")
        harf = input("Bitta harf kiriting:")
        if harf in eski_harf:
            print("Bu harfni oldin kiritgansiz boshqa harf kiriting.")
            continue
        elif harf in list(soz):
            soz_harflari.remove(harf)
            print(f"{harf} harfi to'g'ri")
        else:
            print("Bunday harf yo'q")
        eski_harf += harf
    print(f"Tabriklayman siz {soz} so'zini {len(eski_harf)} ta urinishda topdingiz")
    
        