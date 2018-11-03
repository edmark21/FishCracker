from __future__ import print_function
from colorama import init, Fore

init()
import os,sys
os.system('cls')
os.system("logo.py")
def main():
    print (Fore.GREEN + "              ------------------------------------------------")
    print ("            (                  Password Attack                 )")
    print ("              ------------------------------------------------\n\n\n" + Fore.RESET)
    print (Fore.YELLOW + " 1) Password Recovery")
    print (" 2) Facebook Bruteforce Attack")
    print ("\n\n\n 3) Back" + Fore.RESET)
    s = raw_input(Fore.MAGENTA + "\n\n\n Select Option: " + Fore.RESET)
    if s == '1':
        os.system('cls')
        print (Fore.YELLOW+  "                          Select Target\n\n\n")
        print ("         chats        =         Run chats module")
        print ("         mails        =         Run mails module")
        print ("         git          =         Run git module")
        print ("         svn          =         Run svn module")
        print ("         database     =         Run database module")
        print ("         windows      =         Run windows module")
        print ("         wifi         =         Run wifi module")
        print ("         sysadmin     =         Run system admin module")
        print ("         browsers     =         Run browser module")
        print ("         games        =         Run games module")
        print ("         memory       =         Run memory module")
        print ("         pHP          =         Run php module")
        print ("         maven        =         Run maven module")
        print ("         all          =         Run all module\n\n\n")
        print ("         2)           =         Facebook Password Recovery\n")
        print ("         return       =         Back to menu\n\n\n")
        select = raw_input(Fore.MAGENTA + " Select Target: " + Fore.RESET)
        if select =='2':
            os.system("cls")
            os.system("recover.py")
        elif select == 'return' or  select == 'Return' or  select == 'RETURN':
            os.system("pa.py")
        os.system("laZagne.py " + select)
        raw_input("\n\n\n\n Press Enter to Continue: ")
        os.system('cls')
        os.system("logo.py")
        main()
    if s == '2':
        os.system('fb.py')
    elif s == '3':
        os.system("fc.py")
    else:
        print (" Invalid Command!")
        main()

main()
    
