import requests
import json
from classes.bcolors import bcolors



PROXY = {"http":"socks5://127.0.0.1:9050"}


def checkIPs():
    """
    This funciton checks first the Public IP and then the TOR IP and prints them out.
    """
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


def checkLink(link):
    websiteObj = requests.get(link, proxies=PROXY)
    response_code = websiteObj.status_code
    if response_code == 200:
        status = 'OK'
    else:
        status = 'Failed'

    print("Link: ", link, "\nStatus:", bcolors.OKGREEN + status + bcolors.ENDC )


