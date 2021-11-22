import requests, json
import csv

import sys
import time
import re
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# url = "https://www.tagesschau.de/newsticker.rdf"
# r = requests.get(url, headers=headers)
# c = r.content
# soup = BeautifulSoup(c, features='xml')
# title = soup.find_all('title')
# desc = soup.find_all("description")

def hackernews_rss():
    article_list = [['Titel', 'Description','Category']]
    r = requests.get('https://www.tagesschau.de/xml/rss2/')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
   
   

    
    for a in articles:
       
        
        title = a.find('title').text.replace(',', '')
        description=a.find("description").text.replace(',', '')
        category= re.search("https://.*/(\w*)/",a.find('link').text).group(1);
        article = [title,
                description,category]

                
        article_list.append(article)

    print(len(article_list))
    return article_list


list =hackernews_rss()



#print(list[1][0])

# with open('news.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line)

with open('news.csv', 'w',newline='') as new_file:
        

        csv_writer = csv.writer(new_file, delimiter='\t')

        
        csv_writer.writerows(list)