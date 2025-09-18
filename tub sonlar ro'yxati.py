# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 22:00:15 2025

@author: user
"""

son1 = int(input("Son kiriting: "))
son2 = int(input("Yana son kiriting: "))
tub_sonlar= []
def tub_son(son1,son2):
    """Berilgan sonlar orasida bo'lgan tub sonlarni aniqlovchi funksiya"""
    for n in range(son1,son2+1):
        tub = True
        if n==1:
            tub =False
        elif n==2:
            tub =True
        else:
            for x in range(2,n):
                if n%x ==0:
                    tub=False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar
print(tub_son(son1,son2))
               