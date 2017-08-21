#!/usr/bin/python3
"""
This script will check a list of onion links if they are online or not.
Then returns a list with the pages that are online. 
"""

#import socks
import os
from sys import argv, exit
import requests
from classes.bcolors import bcolors
from classes.checkCl import checkIPs, checkLink


print(bcolors.FAIL + "="*50 + bcolors.ENDC)
print(bcolors.OKGREEN + "Onion Link validator " + bcolors.ENDC)
print(bcolors.FAIL + "="*50 + bcolors.ENDC)


checkIPs()

try:
    filename = argv[1]
except:
    print(bcolors.FAIL + "I need a file with onion Links" + bcolors.ENDC)
    exit(1)


current_path = os.getcwd()
file_path = current_path + "/" + filename

onion_link_file = open(file_path, 'r+')

for line in onion_link_file:
    checkLink(line.strip())

onion_link_file.close()
