# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 05:37:12 2025

@author: user
"""
shaxslar = []
while True:

    ism = input("Marhamat ismiongiz: ")
    familiya = input("Endi familiyangizni kiriting")
    t_yil = input("Tug'ilgan yilingizni kiriting: ")
    t_joy = input("Endi joyingizni: ")
    def malumot(ism,familiya,t_yil,t_joy):
        malumotlar = {'ismi':ism,'familiyasi':familiya,'t_yili':t_yil,'t_joyi':t_joy}
        return malumotlar
    shaxslar.append(malumot(ism, familiya, t_yil, t_joy))
    qoshimcha = input("Yana malumot kiritasizmi: yes/no: ")
    if qoshimcha == 'no':
        break
print(shaxslar)
    
    