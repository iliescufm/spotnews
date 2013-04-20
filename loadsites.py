#	SpotNews | Loadsites - modul citire fisier configurare siteuri si filtre.
#	v0.0.1
#
#	Florin-Mihai Iliescu, e-mail: office@infologica.ro, mobil: (004) 0723233317
#	Raspberry HACK, 20-21 aprilie 2012, Crystal Palace Ballroms - Bucuresti
def loadsites_data():
 filename = 'sites.info'

 try:
    txt = open('sites.info')
    lines = txt.readlines()
    txt.close()
    print lines
 except:
    print "ATENTIE: Nu exista fisierul %s" % filename

 sites_url = []
 sites_filters = []

 for l in lines:
     elem = l.split(',')
     sites_url.append(elem[0])
     sites_filters.append(elem[1].strip())
 return sites_url, sites_filters
