#!/usr/bin/python3

#import socks
#import os
from sys import argv, exit
import subprocess
import requests
from classes.bcolors import bcolors
from classes.checkIP import checkIPs

"""
This script will check a list of onion links if they are online or not.
Then the user will be able to open the link in his Tor browser by clicking on the "Visit" icon.
"""

print(bcolors.FAIL + "="*50 + bcolors.ENDC)
print(bcolors.OKGREEN + "Onion Link validator " + bcolors.ENDC)
print(bcolors.FAIL + "="*50 + bcolors.ENDC)


checkIPs()


try:
    filename = argv[1]
except:
    print(bcolors.FAIL + "I need a file with onion Links" + bcolors.ENDC)
    exit(1)



