import requests
import json
from classes.bcolors import bcolors

def checkIPs():
    # Variable definitions
    PROXY = {"http":"socks5://127.0.0.1:9050"}
    myip = requests.get("http://httpbin.org/ip")

    try:
        torIP = requests.get("http://httpbin.org/ip", proxies=PROXY)
    except NameError:
        print(bcolors.FAIL + "proxy isn't running or address:port is wrong.\nScript will exit." + bcolors.ENDC)
        exit(1)

    jsonIP =json.loads(myip.text)
    jsonTorIP = json.loads(torIP.text)

    print("Your real IP Address is: " + bcolors.OKBLUE + jsonIP["origin"] + bcolors.ENDC)
    print("Your Tor IP Address is: " + bcolors.FAIL + jsonTorIP["origin"] + bcolors.ENDC)
    print(bcolors.FAIL + "="*50 + bcolors.ENDC)



