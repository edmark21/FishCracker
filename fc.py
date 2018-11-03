from __future__ import print_function
from colorama import init, Fore
init()
import os
import sys
import time
time.sleep(1.0)
os.system('cls')

    
    
if sys.platform == 'win32':
    print(Fore.GREEN + "Windows Detected 32bit")  ##Windows 32-bit Check
    time.sleep(2.0)
    macs = 'getmac'
    opt = 'win'
    
    
else:
    sys.platform == 'win64'
    print(Fore.RED + "Window Detected 64 bit")  #64bit
    macs = 'getmac'
    opt = 'win'
    
    


print (Fore.RED + "\n\n\n                                 ##")
print ("                                ### ")                         
print ("                                E@ @#  ")                      
print ("                                ####@@ ")                      
print ("                                 ####@@ ")                     
print ("                                 @#@#@@@#  ")                  
print ("                                  #@@     ")                   
print ("                                    #@ @#####@ ##@# ")         
print ("           #                 ############## ######### ")       
print ("           0#@               ##@@########@### @#@######   ")   
print ("              @#       #   ##@######@##@@##########@####  ")   
print ("           @@@@0##0    #E#@###0E##@@E#@#@###@@### ######@  ")  
print ("             ##@# ##  ####   ######@E#@E@ @# @###  ##@#### ")  
print ("           ###@@@ ##@#@##@   00E@##@ 0#0# @# ####  #@#@###@ ") 
print ("              #@@ #### #       @@E## 000# #0 @###########@#@0")
print ("           #@#########            ####0E0 #0#@###############")
print ("             ### @ @##            @#0###  # 0#############@#0")
print ("           E@# #@###              # # #E0 #  @@#@#########@# ")
print ("               # @##                @ @ @@#E ###@###@@##  #  ")
print ("             @  # ###              ##@#@###0 @@###@# @ E     ")
print ("               E###@E               #@###@ # @@####@   # E   ")
print ("               # ###                 ##@@  # #### ####@  #   ")
print ("                ###E               #@0#@       #######@ #@#  ")
print ("                @##                  ##        ###@@####@#@  ")
print ("               #                   #@            #@@@@#####  ")
print ("              #                  ###                  ####   \n\n" + Fore.RESET)


print (Fore.GREEN + "                               _______________  ")
print (Fore.GREEN + "                               | Version 1.1 |          ")                            
print (Fore.GREEN + "              -------------------------------------------------")
print (Fore.GREEN + "             (                   PISH CRACKER                  )")
print (Fore.GREEN + "              -------------------------------------------------")
print (Fore.CYAN + "                                |     BY     |")
print (Fore.CYAN + "                           -------------------------")
print (Fore.YELLOW + "                          <   EDMARK JAY SUMAMPEN  >")
print (Fore.CYAN + "                           -------------------------")

def main():
    print (Fore.YELLOW + "\n\n                                    Attacks" + Fore.RESET)
    print (Fore.GREEN + "\n\n  1) Wireless Attack")
    print ("  2) Password Attack")
    print ("  3) Social Engineering Attack")
    print ("  4) Information Gathering")
    print ("  5) About")
    print ("  6) Exit" + Fore.RESET)
    s = raw_input(Fore.MAGENTA + "\n Select your Choice: " + Fore.RESET)
    os.system('cls')
    if s == '2':
        os.system('pa.py')
    elif s == '1':
        os.system('wireless.py')
    elif s == '3':
        os.system('se.py')
    elif s == '4':
        os.system('ig.py')
    elif s == '5':
        print ("\n\n\n\n\n\n                          Created by: Edmark Jay Sumampen")
        print ("                           All Rights Reserved 2017-2018\n")
        print ("                               Special Thanks to the \n")
        print ("                               Developers of Weeman")
        print ("                             Http server for Phishing")
        print ("                                Copyright Hypsurus\n\n")
        print ("                            Developers of the laZagne")
        print ("            retrieve lots of passwords stored on a local computer")
        print ("                                       Copyright")
        raw_input("\n\n\n\n\n\n\n Press enter to continue ")
        os.system('fc.py')
    elif s == '6':
        print ("BYE BYE")
        exit()
    else:
        print (" Invalid command")
        time.sleep(2.0)
        os.system('fc.py')
        

main()

