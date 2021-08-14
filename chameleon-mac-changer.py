#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Bukalemun MAC Degistirici")
print("""
Github: https://github.com/Pantheack

Bukalemun MAC Adres Değiştirme Programına Hoş Geldiniz.

1) MAC Adresi Rastgele Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orijinal Haline Döndür
""")

islemno = input("İslem No Girin: ")

if(islemno=="1"):
    os.system("sudo ip addr")
    os.system("sudo ip link set dev eth0 down")
    os.system( "sudo macchanger -r eth0")
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mYeni MAC Adresi Rastgele Belirlendi.")



if(islemno=="2"):
    macadres = input("Yeni MAC Adresini Girin: ")
    os.system("sudo ip addr")
    os.system("sudo ip link set dev eth0 down")
    os.system("sudo macchanger --mac" + macadres + "eth0") 
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mYeni MAC Adresi Manuel Şekilde Belirlendi.")



if(islemno=="3"):
    os.system("sudo ip addr")
    os.system("sudo ip link set dev eth0 down")
    os.system( "sudo macchanger -p eth0")
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mMAC Adresi Orijinal Haline Döndürüldü.")

else:
      print("Hatalı Tuşlama Yaptınız. Program Yeniden Çalıştırılıyor.")
      os.system("python chameleon-mac-changer.py")
