#!/usr/bin/python
# -*- coding : utf-8- -*-
import time
import sqlite3
import fileinput
import moduleCrise
import parseur


def data():

	#Recuperation du fichier txt
	liste = [None] * 9
	i = 0
	with open("ressondee1.txt","r") as fi:
		for line in fi:
			for word in line.split():
				liste[i]=word
				i += 1
	fi.close

	#Connection
	conn=sqlite3.connect('bdd.db')
	cursor = conn.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS donnee(
		nom_machine TEXT,
		cpu_utiliser INTEGER,
		nombre_utilisateurs_connecter INTEGER,
		nombre_processus INTEGER,
		disque_utiliser INTEGER,
		date DATE,
		heure INTEGER,
		swap INTEGER,
		memoire_utiliser INTEGER
		)''')

	

	#Cela permet de supprimer les donnees qui sont dates de plus d'une heure
	cursor.execute("DELETE FROM donnee WHERE heure != strftime('%H','now')+5")

	#Insertion des valeurs de la liste
	cursor.execute("INSERT INTO donnee VALUES(?,?,?,?,?,?,?,?,?+2)",liste)

	#Afficher la Base de donnee(data)
	for row in cursor.execute('SELECT * FROM donnee'):
		print (row)

	cursor.execute("""SELECT 'cpu_utiliser', 'memoire_utiliser', 'disque_utiliser', date FROM donnee""")
	bdd = cursor.fetchone()



	moduleCrise.crise(99,99,99)

	conn.commit()
	conn.close()

def dataPars():
	#Recupere les informations du parseur qui seront mis dans la liste
	ma_liste = parseur.parseur()

	#Connection a la Base de donnees (data)
	conn= sqlite3.connect('Alerte.db')
	cursor = conn.cursor()

	#Creation de la Table 
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Alerte (
		Alerte TEXT,
		date DATE
		)''')

	#Cela permet de supprimer l'ancienne alerte qui est stocke
	cursor.execute("DELETE FROM Alerte")

	#cursor.execute("INSERT INTO Alerte VALUES(?,?)",ma_liste)

	#Affiche la Base de donnee (data)
	for row in cursor.execute("SELECT * FROM Alerte"):
		print(row)

	conn.commit()
	conn.close()