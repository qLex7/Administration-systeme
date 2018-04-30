#!/usr/bin/python
# -*- coding : utf-8- -*-

import os
import sys
import time
import sonde2
import sonde3
import interface
import data

from time import gmtime, strftime


while 1:
	os.system('clear')
	sonde2.sonde2()
	sonde3.sonde3()
	data.data()
	data.dataPars()
	interface.graph()





	time.sleep(15)