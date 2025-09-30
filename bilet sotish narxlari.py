# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 06:59:23 2025

@author: user
"""

savol = "Yoshingizni kiriting: "
savol += "chiqish uchun exit yoki quit deb yozing:  "
while True:
    yosh = input(savol)
    if yosh == 'exit' or yosh =='quit':
        break
    
        
    if int(yosh) < 7:
        narx = 2000
    elif int(yosh) >= 7 and int(yosh) <18:
        narx = 3000
    elif int(yosh) >= 18 and int(yosh) <65:
        narx = 10000
    elif int(yosh) >= 65:
        narx = 0
            
    print("bilet narxi", narx)
    