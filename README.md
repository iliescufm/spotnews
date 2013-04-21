spotnews
========

Bring up the news you value.

Autor: Florin-Mihai Iliescu, e-mail: office@infologica.ro, mobil: (004) 0723233317

Categorie: Software | Agregator de RSS cu filtrare

Link github: https://github.com/iliescufm/spotnews

Aplicatia afiseaza informatiile din fluxurile RSS care contin anumite cuvinte cheie.
Fluxurile RSS is cuvintele cheie sunt preluate din fisierul de configurareb sites.info.

In sites.info pentru fiecare flux RSS se introduce un rand in urmatorul format:
[url rss], [cheie1]+[cheie2]+[cheie3]+...+[cheien]

python spotnews1.py

Genereaza spotnews.html

Pentru a rula trebuie inslate librariile:

pasul 1) chmod +x setuptools-0.6c11-py2.7.egg | sudo ./setuptools-0.6c11-py2.7.egg
pasul 2) cd feedparser-5.1.3 | sudo python setup.py install
pasul 3) cd cd mechanize-0.2.5 | sudo python setup.py install
