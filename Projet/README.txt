   ############################################################
 #### Projet réalisé par Debord Guillaume et Principato Marc ####
   ############################################################


  ################
####   ETAPE 1  ####
  ################

1er sonde : sonde1.sh
	Aucune librairie a été utilisée, toutes les commandes sont en bash.

2eme sonde : sonde2.py
	Nous avons utilisées comme librairie : psutil, socket(Cela permet d'obtenir le nom de la machine) et time.

3eme sonde : sonde3.py
	Nous avons utilisées comme librairie : subprocess, time, os , sys.

Ces trois sondes récupere les mêmes informations: Nom de la machine, le % du Cpu utilisé, le % de la Mémoire utilisé, le % du swap utilisé, le % Disk utilisé, le nombre d'utilisateur connecté, le nombre de processus, la date et l'heure.
Toutes ces données sont mises dans un fichier .txt.


  ################
####   ETAPE 2  ####
  ################


Base de données : data.py
	Nous avons utilisées comme librairie : sqlite3, fileinput, time.

La base de données ouvre le fichier txt et prend les données de la sonde pour les insérer dans la base de donnée crée grâce à sqlite3.
Le fichier .db qui est créée sera stocker sur le disque dur.
Nous avons défini une requête qui permet de supprimer les données qui date de plus d'une heure.


Le Parseur :  parseur.py
	Nous avons utilisées comme librairie : urllib2, BeautifulSoup.
Le parseur récupere et envoie à la base de donnée (data.py) la dernière alerte du site https://www.cert.ssi.gouv.fr.

  ################
####   ETAPE 3  ####
  ################


Module de détection de crise : moduleCrise.py
	Nous avons utilisées comme librairie : time, datetime.
	La fonction recevant en arguments les données qui permettent de détecter une situation de crise
		crise(cpu,memoire,disque)
	Le module fait appel  au moduleMail en cas de crise détecter.


Module d'envoi de mail : moduleMail.py
	Nous avons utilisées comme librairie : smtplib, sys, os , getpass, email.mime.multipart, email.mime.text.
		Le module permet d'envoyé des emails via le serveur smtp de l'université.
		Le contenu de l'email est paramétrable.

Module d'affichage : graph.py
	Nous avons utilisées comme librairie : sqlite3, pygal, datetime, os , sys.
	

