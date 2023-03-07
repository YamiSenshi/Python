#!/usr/bin/env python

import subprocess

#We used raw_input to ensure that the program can run on python 2 too
interface = raw_input("What interface are you using? > ")
new_mac = raw_input("What should be your New MAC? > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

#Previous class on using subprocess.call and can be manipulated in python2
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

#best way of using subprocess.call
#This ensures that the program cannot be manipulated while in python2
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("Your new mac is > " + new_mac)
