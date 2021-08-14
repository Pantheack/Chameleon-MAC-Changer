#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Chameleon MAC Changer")
print("""
Web Site: https://pantheack.github.io/

Github: https://github.com/Pantheack

Welcome to the chameleon mac changer.

1) Set Random MAC Address
2) Set Manual MAC Address
3) Restore Original MAC Address
""")

islemno = input("İslem No Girin: ")

if(islemno=="1"):
        os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
    print("\033[92mYour Mac address has been randomly assigned.")



if(islemno=="2"):
    macadres = input("Yeni Mac Adresini Giriniz > ")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac "+macadres+" eth0")
		os.system("ifconfig eth0 up")
    print("\033[92mYour Mac address has been manually assigned.")



if(islemno=="3"):
        os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
    print("\033[92mMAC Address Restored To Its Original State.")

else:
      print("You made a wrong keystroke. The program will restart.")
      os.system("python chameleon-mac-changer.py")
