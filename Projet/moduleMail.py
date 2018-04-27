#!/usr/bin/python
# -*- coding : utf-8- -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



def mail(mes):
	
	#-------------Creation d'un message-------------
	msg = MIMEMultipart()


	#----------Les parametres du message------------ 

	password = "4Fc275113"
	msg['From'] = "guillaume.debord@alumni.univ-avignon.fr"
	msg['To'] = "guillaume.debord@alumni.univ-avignon.fr"
	msg['Subject'] = "Alerte"

	#----------Creation du serveur------------------
	mailserver = smtplib.SMTP_SSL('smtpz.univ-avignon.fr:465')


	message = mes
	msg.attach(MIMEText(message))

	mailserver.ehlo()


	#-------------Connexion----------------
	mailserver.login(msg['From'], password)

	#--------------------Envoie du message----------------------
	mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

	mailserver.close()

	print "successfully send email to %s" %(msg['To'])











