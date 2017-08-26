import re
import certifi
import urllib3
from urllib3.contrib.socks import SOCKSProxyManager
import json
from classes.bcolors import bcolors



#PROXY = {"http":"socks5://127.0.0.1:9050"}


def checkIPs():
    """
    This funciton checks first the Public IP and then the TOR IP and prints them out.
    """
    proxy = SOCKSProxyManager('socks5h://localhost:9050/')
    http = urllib3.PoolManager()
    myip = http.request('GET', 'http://httpbin.org/ip')

    try:
        torIP = proxy.request('GET', 'http://httpbin.org/ip')
    except NameError:
        print(bcolors.FAIL + "proxy isn't running or address:port is wrong.\nScript will exit." + bcolors.ENDC)
        exit(1)

    #print(myip.data)
    #print(str(myip.data))
    jsonIP =json.loads(myip.data.decode('utf-8'))
    jsonTorIP = json.loads(torIP.data.decode('utf-8'))

    print("Your real IP Address is: " + bcolors.OKBLUE + jsonIP["origin"] + bcolors.ENDC)
    print("Your Tor IP Address is: " + bcolors.FAIL + jsonTorIP["origin"] + bcolors.ENDC)
    print(bcolors.FAIL + "="*50 + bcolors.ENDC)

def checkLink(link):
    try:
        proxy = SOCKSProxyManager('socks5h://localhost:9050/') #, cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        websiteObj = proxy.request('GET', link, timeout=3.0)
        response_code = websiteObj.status
    except:
        response_code = 500
        pass

    if response_code >= 200 and response_code <= 299:
        status = 'OK'
        print("Link: ", bcolors.OKBLUE +  link + bcolors.ENDC , "\nStatus:", bcolors.OKGREEN + status + bcolors.ENDC )
    elif response_code >= 500:
        status = 'Failed'
        print("Link: ", bcolors.FAIL + link + bcolors.ENDC, "\nStatus:", bcolors.FAIL + status + bcolors.ENDC )


def extrOnionLink(link):
    pattern = re.compile(r'(.+.onion)')
    matchObj = re.search(pattern, str(link))
    link = matchObj.group(1)
#    link = "http://"+link.strip()
    return link





"""
#test function work.

def checkLink2(link):
    try:
        http = urllib3.PoolManager()
        websiteObj = http.request('GET', link)
        response_code = websiteObj.status
    except:
        response_code = 500
        pass

    if response_code >= 200 and response_code <= 299:
        status = 'OK'
        print("Link: ", link, "\nStatus:", bcolors.OKGREEN + status + bcolors.ENDC )
    elif response_code >= 500:
        status = 'Failed'
        print("Link: ", link, "\nStatus:", bcolors.FAIL + status + bcolors.ENDC )
"""
