#import socks
#import os
from sys import argv
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


PROXY = {"http":"socks5://127.0.0.1:9050"}

myip = requests.get("http://httpbin.org/ip")
jsonIP =json.loads(myip.text)
print("Your real IP Adress is: " + bcolors.OKBLUE + jsonIP["origin"] + bcolors.ENDC)
torIP = requests.get("http://httpbin.org/ip", proxies=PROXY)
jsonTorIP = json.loads(torIP.text)
print("Your Tor IP Adress is: " + bcolors.FAIL + jsonTorIP["origin"] + bcolors.ENDC)
print(bcolors.FAIL + "="*50 + bcolors.ENDC)


linkList = []

