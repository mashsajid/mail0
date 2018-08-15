#!/usr/bin/python

import os
import subprocess
import sys
from colors import *
try:
	while True:



		os.system("clear")
		file = open("mail0", "r") 	
		sys.stdout.write(RED)
		print file.read()			
		
		print ('0.Send')
		sys.stdout.write(GREEN)
		print('1.Quit')
		sys.stdout.write(BOLD)
		user_input_menu=input()

		if user_input_menu==0:
			os.system("clear")
			while True:

							sys.stdout.write(GREEN)
							print file.read()
							Fake=raw_input("  Fake Email Address: ")
                                                        Terget=raw_input("     Terget Email: ")
							subject=raw_input("     Subject: ")
							mass=raw_input("     Massage: ")
							ser=raw_input("     SMTP Server: ")
							usr=raw_input("     Username: ")
							psw=raw_input("     Password: ")
							tls=raw_input("   Do you want tls? Y/N:  ")
							
							if tls=="y":
							     os.system("clear")
							     print ("Sending the mail......")
                                                            
							subprocess.call(["./sendEmail","-f",Fake,"-t",Terget,"-u",subject,"-m",mass,"-s",ser,"-xu",usr,"-xp",psw])
                                                        
                                                        if tls=="n":
                                                             os.system("clear")
                                                             print ("Sending the mail......")
                                                             
                                                             subprocess.call(["./sendEmail","-f",Fake,"-t",Terget,"-u",subject,"-m",mass,"-s",ser,"-xu",usr,"-xp",psw,"-o","tls=no"])
                                                        
                                                        break
                                                        
                                                        

				
		elif user_input_menu==1: 
			sys.stdout.write(BOLD)
			print ('Good Bye!!')
			break

except KeyboardInterrupt:
	sys.exit(0) # or 1, or whatever
