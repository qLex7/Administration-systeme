#!/usr/bin/env python
import smtplib
import sys
import os
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Ceci est les parametres du mail
def parametro():
    
    print("Enregistrer les nouveaux parametres emails:")
     
    print("Votre adresse:")
    From = sys.stdin.readline()
    print("Destinataire")
    To = sys.stdin.readline()
    print("Votre mot de passe:")
    Mdp = sys.stdin.readline()
    mon_fichier = open("parametroMail.txt", "w")
    mon_fichier.write(From)
    mon_fichier.write(To)
    mon_fichier.write(Mdp)
    print("Parametre sauvegarde")
    mon_fichier.close()
    

#Ceci est la creation du serveur Mail
def endiar(typ,mes):
    mon_fichier = open("parametroMail.txt", "r")
    user = mon_fichier.read().split('\n')
    
    if os.path.getsize("parametroMail.txt") == 0:
        print("Vos parametre sont vides")
        parametro()
        
    msg = MIMEMultipart()
    msg['From'] = user[0]
    msg['To'] = user[1]
    msg['Subject'] = 'Alerte:' + typ
    

    mailserver = smtplib.SMTP_SSL('smtpz.univ-avignon.fr:465')
    message = mes
    msg.attach(MIMEText(message))

    mailserver.ehlo()
    mailserver.login(user[0], user[2])

    #Cela permet d'envoyer le mail
    mailserver.sendmail(user[0], user[1], msg.as_string())   
    mailserver.close()
    print "successfully sent email %s" %(msg['To'])
    mon_fichier.close()











