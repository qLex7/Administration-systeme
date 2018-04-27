#!/usr/bin/python
# -*-coding:Latin-1 -*
import psutil
import socket
from time import gmtime,strftime

def sonde2():
	donnees = list()
	
	#-----------Nom de la machine---------------
	donnees.append(socket.gethostname())
	
	#-----------Cpu utilisé en %----------------
	donnees.append(psutil.cpu_percent(interval=1))
	
	#-----------Nombre Users--------------------
	donnees.append(len(psutil.users()))

	#-----------Nombre de processus-------------
	donnees.append(len(psutil.pids()))

	#-----------MémoireUtilisé--------------------
	donnees.append(psutil.virtual_memory().percent)

	#-----------Disque utilisé en %-------------
	donnees.append(psutil.disk_usage('/').percent)
		
	#----------------Date----------------------
	donnees.append(strftime("%Y-%m-%d:%H:%M:%S",gmtime()))

	#-----------------Heure--------------------
	donnees.append(strftime("%H",gmtime()))

	#--------------SwapTotal--------------------
	donnees.append(psutil.swap_memory().percent)

	
	
	
	mon_fichier = open("ressondee1.txt","w")
	for item in donnees:
		mon_fichier.write("%s\n" %item)
	mon_fichier.close()