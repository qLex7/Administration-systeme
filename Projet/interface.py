#!/usr/bin/python
# -*-coding: Latin-1 -*-
import os
import sys
import pygal
import sqlite3
from datetime import datetime, timedelta

def graph():

	conn = sqlite3.connect('sonde.db')
	cursor = conn.cursor()

	hostname=list()
	n=5

	for row in cursor.execute('SELECT DISTINCT hostname FROM donnee'):
		hostname.append(row)

	for name in hostname:
		for row in cursor.execute("""SELECT cpu_utiliser, memoire_utiliser, disque_utiliser,nombre_utilisateur_connecter, swap time FROM donnee"""):
			
			data = cursor.fetchone()
			bar_chart = pygal.Bar()
			bar_chart.title = 'Donnees utilisateur'
			bar_chart.x_labels = map(str, range(1,n))
			bar_chart.add('Utilisateur', data[3])
			bar_chart.add('Swap', data[4])
			bar_chart.add('Cpu',  data[0])
			bar_chart.add('Mem', data[1])
			bar_chart.add('Disque', data[2])
			bar_chart.render_in_browser()