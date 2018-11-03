from __future__ import print_function
from colorama import init, Fore
init()
import os
import sys
import time
import json
import requests
time.sleep(1.0)
os.system('cls')


print (Fore.GREEN + "                               _______________  ")
print (Fore.GREEN + "                               | Version 1.1 |          ")                            
print (Fore.GREEN + "              -------------------------------------------------")
print (Fore.GREEN + "             (               Information Gathering             )")
print (Fore.GREEN + "              -------------------------------------------------")
print (Fore.CYAN + "                                    | BY |")
print (Fore.CYAN + "                           -------------------------")
print (Fore.YELLOW + "                          <   EDMARK JAY SUMAMPEN  >")
print (Fore.CYAN + "                           -------------------------\n\n\n\n")


print (" 1) GeoLocation")
print (" 2) back\n\n")

s = raw_input(' Enter your choice: ')

if s == '1':
    target = raw_input(Fore.CYAN + ' Enter an ip address: ') #User Input
    send_url = 'http://freegeoip.net/json/'+target #Finds Targets
    r = requests.get(send_url) #Sends Url
    j = json.loads(r.text) #Reads All Text
    cn = j['country_name'] #Reads Country
    rc = j['region_code'] #Reads Region Code
    city = j['city'] #Reads City
    lat = j['latitude'] #Read Latitiude
    lon = j['longitude'] #Read Longitude
    print ("  Latitude")
    print (lat)
    print ("  Longitude")
    print  (lon)
    print ("  City")
    print (city)
    print ("  Regional Country")
    print (rc)
    print ("  Country")
    print (cn)
elif s == '2':
    os.system('fc.py')
else:
    print ('Invalid command!')
    time.sleep(2)
    os.system('ig.py')
