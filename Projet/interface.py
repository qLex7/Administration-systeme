#!/usr/bin/python
# -*-coding: Latin-1 -*-
import os,sys
import pygal
import sqlite3
from datetime import datetime, timedelta


def graph():
	conn=sqlite3.connect('sonde.db')

	cursor = conn.cursor()

	hostname = list()
	listCpu = list()
	listMemoire = list()
	listDisque = list()
	listUtilisateur = list()
	listSwap = list()
	n=6



	 
    #Cela permet de séparer l'historique de tous utilisateur
        
    graphDisk = [listeDisque[x:x+n] for x in range(0,len(listeDisque),n)]
        


       
 	#Ces boucles permet de remplir la liste avec tous les noms de toutes les machines ainsi que l'affichage de chaque entrée
        
	for row in c.execute('SELECT DISTINCT hostname FROM sonde'):
        hostname.append(row)

	for name in hostname:
        for row in c.execute('select * from sonde WHERE hostname=? ORDER BY time DESC LIMIT 1',name):
        	print (row)
        

     
    #Toutes les boucles ci-dessous permettent de remplir les liste déjà définis et aussi d'avoir l'historique de toutes les machines
    #- Disque,
    #- Memoire,
    #- Cpu,
    #- Swap,
    #- Utilisateur,
    
    for name in hostname:
        for row in c.execute('SELECT disque from sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
            listDisque.append(row)

    for name in hostname:
        for row in c.execute('SELECT ram FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
            listMemoire.append(row)       
        graphMemoire = [listMemoire[x:x+n] for x in range(0,len(listMemoire),n)]

    for name in hostname:
        for row in c.execute('SELECT cpu FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
            listCpu.append(row)     
        graphCpu = [listCpu[x:x+n] for x in range(0,len(listCpu),n)]
        

    for name in hostname:
        for row in c.execute('SELECT swap FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
            listSwap.append(row)        
        graphSwap = [listSwap[x:x+n] for x in range(0,len(listSwap),n)]


    for name in hostnames:
        for row in c.execute('SELECT utilisateur FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
            listUtilisateur.append(row)
        graphUser = [listUtilisateur[x:x+n] for x in range(0,len(listUtilisateur),n)]

    conn.close()



       
    #Les fonctions ci-dessous permettent de créer un graph des données
    #   - %Disque utilisé,
    #   - %Ram utilisé,
    #   - %CPU utilisé,
    #   - SWAP total,
    #   - Nombre utilisateur connectés
    #Les graph vont être créer via une page HTML, elles se mettront à jour a chaque fois que les sondes vont être relancés
    

    conn = sqlite3.connect('sonde.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT cpu, ram, disque,cpu, swap time FROM sonde""")
    data = c.fetchone()

    bar_chart = pygal.Bar()
    bar_chart.title = 'Donnees utilisateur'
    bar_chart.x_labels = map(str, range(1,n))
    bar_chart.add('Utilisateur', data[0])
    bar_chart.add('Swap', data[4])
    bar_chart.add('Cpu',  data[3])
    bar_chart.add('Mem', data[1])
    bar_chart.add('Disque', data[2])
	bar_chart.render_in_browser()