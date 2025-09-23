# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 21:26:52 2025

@author: user
"""

import random
def sontop(x=10):
    javob=random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi:")
    taxminlar = 0
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if taxmin<javob:
            print("Topa olmadingiz. Men o'ylagan son bundan kattaroq. Yana urinib ko'ring: ")
        elif taxmin>javob:
            print("Topa olmadingiz. Men o'ylagan son bundan kichikroq. Yana urinib ko'ring: ")
        else:
            break
    print(f"Tabriklaymiz siz sonni {taxminlar}ta taxmin bilan topdingiz")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha bitta son o'ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
   
    taxminlar = 0
    while True:
        if quyi !=yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = yuqori
        taxminlar +=1
        javob = input(f"Siz {taxmin} sonini o'yladingiz. Shundaymi? (t,+,-): ")
        if javob == "+":
            quyi =taxmin+1
        elif javob == "-":
            yuqori =taxmin-1
        else:
            break
    print(f"Men javobingizni {taxminlar}ta taxmin bilan topdim".lower())
    return taxminlar
def go_play(x=10):
    davom = True
    while davom:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
    
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        davom = int(input("Yana o'ynaymizmi ha(1)/yo'q(0): "))
    print("O'ynaganingiz uchun raxmat ")