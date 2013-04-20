import feedparser

site_titles = ['CNN.com - Technology', 'Ziarul Financiar']
site_urls = ['http://rss.cnn.com/rss/cnn_tech.rss', 'http://www.zf.ro/rss.xml']

def display_rss_info(url):
 feed = feedparser.parse(url)
 if feed[ "bozo" ] == 1:
    print "Scuze, stirile de la [%s] nu sunt disponibile" % url
 else: 
   print feed[ "url" ] 	#  URL of the feed's RSS feed
   print feed[ "version" ] #  version of the RSS feed
   print feed[ "channel" ][ "title" ] # "PythonInfo Wiki" - Title of the Feed.
   print feed[ "channel" ][ "description" ] # "RecentChanges at PythonInfo Wiki." - Description of the Feed
   print feed[ "channel" ][ "link" ] # Link to RecentChanges - Web page associated with the feed.
   #print feed[ "channel" ][ "wiki_interwiki" ] # "Python``Info" - For wiki, the wiki's preferred InterWiki moniker.
   print "-------------------------------------------------"
   #print feed[ "items" ] # A gigantic list of all of the RecentChanges items.
   idx = 1
   for l in feed[ "items" ]:
      print "ITEM [%s]" % idx
      print "%s - %s" % (l[ "title" ], l[ "published" ]) 
      idx = idx + 1
   print "-------------------------------------------------"

for url in site_urls:
 display_rss_info(url)
