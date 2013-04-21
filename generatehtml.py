# -*- coding: iso-8859-15 -*-
#	SpotNews | GenerateHTML - modul generare fisier html.
#	v0.0.1
#
#	Florin-Mihai Iliescu, e-mail: office@infologica.ro, mobil: (004) 0723233317
#	Raspberry HACK, 20-21 aprilie 2012, Crystal Palace Ballroms - Bucuresti

import datetime

filename  = 'spotnews.html'

def currenttime_string():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

def start_html():
 f = open(filename,"w")
 f.write('<html>\n')
 f.write('<title>SpotNews ' + currenttime_string() + '</title>\n')
 f.write('<body>\n')
 f.close()

def print_h1(text):
 f = open(filename,"a")
 f.write("<h1>%s</h1>\n" % text)
 f.close()

def print_h2(text):
 f = open(filename,"a")
 f.write("<h2>%s</h2>\n" % text)
 f.close()

def print_p(text):
 f = open(filename,"a")
 f.write("<p>%s</p>\n" % text)
 f.close()

def print_url(url,text):
 f = open(filename,"a")
 f.write("<a href=\"%s\">%s</a>\n" % (url,text))
 f.close()

def end_html():
 f = open(filename,"a")
 f.write('</body>\n')
 f.write('</html>\n')
 f.close()
