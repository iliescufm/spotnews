# -*- coding: iso-8859-15 -*-

#	SpotNews | aplicatie principala.
#	v0.1.0
#
#	Florin-Mihai Iliescu, e-mail: office@infologica.ro, mobil: (004) 0723233317
#	Raspberry HACK, 20-21 aprilie 2012, Crystal Palace Ballroms - Bucuresti

import feedparser, re, time

import codecs

from browse import browse_url
from loadsites import loadsites_data
from generatehtml import *

(site_urls, site_filters) = loadsites_data()

def print_feed_data_to_html(feed,filters):
   idx = 1
   keys = filters.split('+')
   print_h1(feed[ "channel" ][ "title" ]+" ["+filters.replace('+',', ') + "]")
   for l in feed[ "items" ]:
      item_title = l[ "title" ]
      item_descr = re.sub('<[^<]+?>', '', l[ "description" ]).strip()
      printed = False
      for k in keys:
          if not printed and ((k in item_title) or (k in item_descr)):
             h2 = "[%s]: %s - %s" % (idx, item_title.encode('ascii', 'replace'), l[ "published" ])
             print_h2(h2)
             p = item_descr.encode('ascii', 'ignore')
             print_p(p)
             print_url(l[ "link" ],"citeste mai mult...")
             idx = idx + 1
             printed = True

def print_rss_to_html(url):
   feed = feedparser.parse(url)
   if feed[ "bozo" ] == 1:
       print "Scuze, stirile de la [%s] nu sunt disponibile" % url
   else: 
       print_feed_data_to_html(feed,site_filters[site_urls.index(url)])

   
def display_rss_info(url):
   feed = feedparser.parse(url)
   if feed[ "bozo" ] == 1:
       print "Scuze, stirile de la [%s] nu sunt disponibile" % url
   else: 
       print_feed_data(feed,site_filters[site_urls.index(url)])

print site_urls

while 1:
    start_html()
    for url in site_urls:
       print_rss_to_html(url)
    end_html()
    time.sleep(60)
    print currenttime_string() + ": updating..."
