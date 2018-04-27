#!/usr/bin/python
# -*- coding : utf-8- -*-

import time
import datetime
import moduleMail 

def crise(cpu,memoire,disque):

	if cpu > 99:
		moduleMail.mail("Erreur rencontre : Probleme le cpu est trop eleve.")
	

	if memoire > 99:
		moduleMail.mail("Erreur rencontre : Probleme la ram est trop eleve")
		

	if disque > 99:
		moduleMail.mail("Erreur rencontre : Probleme la capacite max du Disque a etait atteinte")
		

	
	



