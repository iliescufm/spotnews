# coding: utf-8

#	SpotNews | Browse - modul interpretare text in legatura cu titlul.
#	v0.0.1
#
#	Florin-Mihai Iliescu, e-mail: office@infologica.ro, mobil: (004) 0723233317
#	Raspberry HACK, 20-21 aprilie 2012, Crystal Palace Ballroms - Bucuresti

from mechanize import Browser
import re

def browse_url(title,site_url):

 debug = False;

 title_words = [];

 def remove_nonsense(words):
    words_with_sense = [];
    for k in words:
	if len(k)>3:
	    words_with_sense.append(k)
    if debug:
	if len(words_with_sense) == 0:
	    print "ATENTIE: S-ar putea sa avem o problema, nimic nu are sens in fraza [%s]" % words	
    return words_with_sense;

 def text_in_scope(text):
    matched = 0
    text_words = text.split()
    title_words_number = len(title_words)
    for k in title_words:
        for w in text_words:
            if (k == w) or ((len (k) > 3 or len(w) > 3) and ((k in w) or (w in k))):
                matched = matched + 1 
    		if debug:
		    print "DEBUG: (%s,%s)" % (k,w)
    if (len(text_words)>2) and (matched > 0):
	return True
    else:
	return False

 title_words = remove_nonsense(title.split())

 if debug:
    print title_words
 br = Browser()
 br.open(site_url)
 html = br.response().readlines()
 p_tag = False
 for line in html:
    if '<p' in line or p_tag:
        p_tag = not p_tag
        text = re.sub('<[^<]+?>', '', line)
        text = text.strip()
        text = text.replace('&nbsp;','')
        if debug:
            print "DEBUG:" + text
            print "-----------------------------------"
        if text_in_scope(text):
	    print text
            title_words = title_words + remove_nonsense(text.split())
            if debug:
                print "DEBUG: %s" % title_words
