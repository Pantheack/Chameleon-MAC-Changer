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

islemno = input("Enter the process number: ")

if(islemno=="1"):
    os.system("sudo ip link set dev eth0 down")
    os.system("sudo macchanger -r eth0")
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mYour Mac address has been randomly assigned.")



if(islemno=="2"):
    macadres = input("Enter the new MAC address: ")
    os.system("sudo ip link set dev eth0 down")
    os.system("sudo macchanger --mac" + macadres + "eth0") 
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mYour Mac address has been manually assigned.")

if(islemno=="3"):
    os.system("sudo ip link set dev eth0 down")
    os.system( "sudo macchanger -p eth0")
    os.system("sudo ip link set dev eth0 up")
    print("\033[92mMAC Address Restored To Its Original State.")

else:
      print("You made a wrong keystroke. The program will restart.")
      os.system("python chameleon-mac-changer.py")
