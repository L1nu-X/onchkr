#!/usr/bin/python3

#import socks
#import os
from sys import argv, exit
import json
import urllib3
import requests
from classes.bcolors import bcolors

"""
This script will check a list of onion links if they are online or not.
Then the user will be able to open the link in his Tor browser by clicking on the "Visit" icon.
"""

print(bcolors.FAIL + "="*50 + bcolors.ENDC)
print(bcolors.OKGREEN + "Onion Link validator " + bcolors.ENDC)
print(bcolors.FAIL + "="*50 + bcolors.ENDC)

try:
    filename = argv[1]
except:
    print(bcolors.FAIL + "I need a file with onion Links" + bcolors.ENDC)
    exit(1)

# Variable definitions
PROXY = {"http":"socks5://127.0.0.1:9050"}



myip = requests.get("http://httpbin.org/ip")
torIP = requests.get("http://httpbin.org/ip", proxies=PROXY)

jsonIP =json.loads(myip.text)
jsonTorIP = json.loads(torIP.text)

print("Your real IP Adress is: " + bcolors.OKBLUE + jsonIP["origin"] + bcolors.ENDC)
print("Your Tor IP Adress is: " + bcolors.FAIL + jsonTorIP["origin"] + bcolors.ENDC)
print(bcolors.FAIL + "="*50 + bcolors.ENDC)




