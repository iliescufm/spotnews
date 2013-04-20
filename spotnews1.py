# -*- coding: iso-8859-15 -*-
import feedparser, re

import codecs

from browse import browse_url
from loadsites import loadsites_data

site_titles = ['CNN.com - Technology', 'Ziarul Financiar']
#site_urls = ['http://rss.cnn.com/rss/cnn_tech.rss', 'http://www.zf.ro/rss.xml']
(site_urls, site_filters) = loadsites_data()

def print_feed_data(feed,filters):
   print feed[ "url" ] 	#  URL of the feed's RSS feed
   print feed[ "version" ] #  version of the RSS feed
   print feed[ "channel" ][ "title" ] # "PythonInfo Wiki" - Title of the Feed.
   print feed[ "channel" ][ "description" ] # "RecentChanges at PythonInfo Wiki." - Description of the Feed
   print feed[ "channel" ][ "link" ] # Link to RecentChanges - Web page associated with the feed.
   #print feed[ "channel" ][ "wiki_interwiki" ] # "Python``Info" - For wiki, the wiki's preferred InterWiki moniker.
   print "-------------------------------------------------"
   #print feed[ "items" ] # A gigantic list of all of the RecentChanges items.
   idx = 1
   keys = filters.split('+')
   print keys
   for l in feed[ "items" ]:
      item_title = l[ "title" ]
      item_descr = re.sub('<[^<]+?>', '', l[ "description" ]).strip()
      printed = False
      for k in keys:
          if not printed and ((k in item_title) or (k in item_descr)):
             print "ITEM [%s]: %s - %s" % (idx, item_title.encode('ascii', 'ignore'), l[ "published" ]) 
             print item_descr.encode('ascii', 'ignore')
             print l[ "link" ]
             #browse_url(l[ "title" ],l[ "link" ])
             #print "_________________________________________________"
             idx = idx + 1
             printed = True
   print "-------------------------------------------------"
   
def display_rss_info(url):
   feed = feedparser.parse(url)
   if feed[ "bozo" ] == 1:
       print "Scuze, stirile de la [%s] nu sunt disponibile" % url
   else: 
       print_feed_data(feed,site_filters[site_urls.index(url)])

def rss_test(url):
    feed = feedparser.parse(url)
    if feed[ "bozo" ] == 1:
        print "Scuze, stirile de la [%s] nu sunt disponibile" % url
    else: 
        print feed.entries

print site_urls
  
for url in site_urls:
 #rss_test(url)
 display_rss_info(url)

