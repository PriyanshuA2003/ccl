from bs4 import BeautifulSoup
from urllib.request import urlopen
import mysql.connector
import datetime


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="analyzer"
)


def business_news():
    site = 'https://feeds.feedburner.com/ndtvprofit-latest'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [crypto,market,business,economy,industry,money]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  business_subcategory(buss_sub_id ,Crypto ,Market ,Money ,Economy ,Industry ,Date ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val3 = (id, text, text, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()




def entertainment_news():
    site = 'https://feeds.feedburner.com/ndtvmovies-latest'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [tv,bollywood,hollywood,web series,entertainment,actor,movies]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  entertainment_subcategory(ent_sub_id , bollywood , hollywood , tv , web_series , Date ) VALUES (%s,%s,%s,%s,%s,%s)"
val3 = (id,text, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()




def nation_news():
    site = 'https://feeds.feedburner.com/ndtvnews-india-news'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [covid , nation, governmemt ,court, crime,city, state]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  nation_subcategory(nation_sub_id ,covid ,government ,crime ,court ,Date ) VALUES (%s,%s,%s,%s,%s,%s)"
val3 = (id, text, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()




def sports_news():
    site = 'https://feeds.feedburner.com/ndtvsports-latest'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [cricket,sports,olympics,football,tennis,badminton]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  sports_subcategory(sports_id ,cricket ,football ,tennis ,Date ) VALUES (%s,%s,%s,%s,%s)"
val3 = (id, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()




def technology_news():
    site = 'https://feeds.feedburner.com/gadgets360-latest'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [mobile, new gadgets, crypto,5G, technology, laptop,vfx]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  technology_subcategory(tech_sub_id ,5G ,Mobile ,New_gadgets ,Crypto ,Date ) VALUES (%s,%s,%s,%s,%s,%s)"
val3 = (id, text, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()




def world_news():
    site = 'https://feeds.feedburner.com/ndtvnews-world-news'
    op = urlopen(site)  # Open that site
    r = op.read()  # read data from site
    soup = BeautifulSoup(r.content, features = "html.parser")
    text_li = (''.join(s.findAll(text = True))for s in soup.findAll('li'))	
    counts = Counter((x.rstrip(punctuation).lower() for y in text_li for x in y.split()))
    list_headlines  = counts.most_common()

    keywords = [asia, usa, uk,world, russia, ukraine, india, china]
    for x in range(0, len(list_headlines)):
        temp = list(list_headlines[x]) 
        temp[1] = str(temp[1]) 
        n_temp = [(unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).lower().decode() for word in temp] 	
        hits = 0 
        for i in range(0, len(keywords)):
        	if keywords[i] in n_temp[0]:
                    hits = hits + 1	
        keyword_hits = int(n_temp[1])*int(n_temp[2])
        keyword_counts = sum(keyword_hits)


cursor = mydb.cursor()
sql3="INSERT INTO  world_subcategory(world_sub_id,Russia ,USA ,UK ,Asia ,Date) VALUES (%s,%s,%s,%s,%s,%s)"
val3 = (id, text, text, text, text, str(datetime.datetime.now()))
cursor.execute(sql3, val3)
mydb.commit()