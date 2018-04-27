#!/usr/bin/python
# -*- coding : utf-8- -*-

import urllib2
import BeautifulSoup
from urllib2 import urlopen

def parseur():
	page = urlopen("https://www.cert.ssi.gouv.fr/alerte/feed").read()
	soup = BeautifulSoup.BeautifulSoup(page)
	